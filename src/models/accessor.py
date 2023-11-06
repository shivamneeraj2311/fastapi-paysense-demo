import logging
import typing
import datetime

import pydantic
import sqlakeyset
import sqlalchemy.exc
import sqlalchemy.orm
import sqlalchemy.sql.elements
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Query, Session


from src.database.base import Base

from src.models.entity import Entity
from src.models.id import IdStr

if typing.TYPE_CHECKING:
    from pydantic.typing import AbstractSetIntStr, MappingIntStrAny

ChangeSet = typing.Dict[typing.Union[str, typing.Tuple[str]], typing.Any]


logger = logging.getLogger("default")

O = typing.TypeVar("O", bound=Base)
E = typing.TypeVar("E", bound=Entity)
I = typing.TypeVar("I", bound=int)

custom_sql_alchemy_encoder: typing.Dict[
    typing.Any, typing.Callable[[typing.Any], typing.Any]
] = {
    datetime.datetime: lambda d: d,
    pydantic.SecretStr: lambda s: s.get_secret_value(),
}
def commit(session: Session):
    try:
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        logger.warning(e)
        session.rollback()
        raise Exception()


PaginationKey = typing.Tuple[typing.Sequence[typing.Any], bool]
PaginationParams = typing.Tuple[typing.Optional[PaginationKey], int]


class Page(pydantic.BaseModel, typing.Generic[E]):
    prev_key: typing.Optional[PaginationKey]
    next_key: typing.Optional[PaginationKey]
    items: typing.List[E]
    total_count: typing.Optional[int]


def page_query_results(query: Query, pagination_params: PaginationParams):
    key, offset = pagination_params
    page = sqlakeyset.get_page(query, per_page=offset, page=key)
    assert page.paging is not None
    prev_key: typing.Optional[PaginationKey] = typing.cast(
        PaginationKey,
        page.paging.previous if page.paging.has_previous else None,
    )
    next_key: typing.Optional[PaginationKey] = typing.cast(
        PaginationKey, page.paging.next if page.paging.has_next else None
    )
    return list(page), prev_key, next_key


Q = typing.TypeVar("Q", bound="sqlalchemy.orm.Query")
Querier = typing.Callable[[Q], Q]


def querier_no_op(q: Q) -> Q:
    return q


def querier_fresh(q: Q) -> Q:
    """
    Do not use sqlalchemy identity map and hard pull from db
    """
    return q.populate_existing()


def querier_lock_result(q: Q) -> Q:
    return querier_fresh(q).with_for_update()


Filter = typing.NewType("Filter", sqlalchemy.sql.elements.BinaryExpression)

Filters = typing.Iterable[Filter]


class Accessor(typing.Generic[O, E, I]):
    orm_table: typing.Type[O]
    entity: typing.Type[E]
    # entity: E

    primary_key_col = "id"
    order_col = "create_date"

    exclude_fields: typing.Union["AbstractSetIntStr", "MappingIntStrAny"] = {}

    @classmethod
    def get_by_id(
        cls,
        *,
        resource_id: I,
        db_session: Session,
        populate_existing: bool = False,
        # can be a dictionary of options here https://docs.sqlalchemy.org/en/14/orm/query.html#sqlalchemy.orm.Query.with_for_update
        with_for_update: bool = False,
    ) -> E:
        resp = db_session.get(
            cls.orm_table,
            resource_id,
            populate_existing=populate_existing,
            with_for_update=with_for_update,
        )

        if resp is None:
            raise Exception(f"id={resource_id}")

        return typing.cast(E, cls.entity.from_orm(resp))

    @classmethod
    def get_first_by_filter(cls, *, filters: Filters = (), db_session: Session) -> E:
        q = db_session.query(cls.orm_table).filter(*filters)

        resp = q.first()

        if resp is None:
            raise Exception("multiple filters")

        return typing.cast(E, cls.entity.from_orm(resp))

    @classmethod
    def get_all(
        cls,
        *,
        pagination_params: PaginationParams,
        db_session: Session,
        filters: Filters = (),
    ) -> Page[E]:
        order_col = getattr(cls.orm_table, cls.order_col)
        id_col = getattr(cls.orm_table, cls.primary_key_col)
        q: Query = typing.cast(
            Query,
            db_session.query(cls.orm_table)
            .filter(*filters)
            .order_by(order_col, id_col),  # type: ignore
        )

        count = q.count()

        page, prev_page, next_page = page_query_results(q, pagination_params)
        items = [cls.entity.from_orm(c) for c in page]
        return Page(
            prev_key=prev_page, items=items, next_key=next_page, total_count=count
        )

    @classmethod
    def add(
        cls,
        *,
        entity: E,
        db_session: Session,
        include: typing.Union["AbstractSetIntStr", "MappingIntStrAny"] = None,
        exclude: typing.Union["AbstractSetIntStr", "MappingIntStrAny"] = None,
    ) -> None:
        obj_in_data = jsonable_encoder(entity, custom_encoder=custom_sql_alchemy_encoder)
        entity_orm = cls.orm_table(**obj_in_data)
        db_session.add(entity_orm)
        db_session.commit()
        db_session.refresh(entity_orm)

    @classmethod
    def update_by_id(
        cls, *, resource_id: I, change_set: ChangeSet, db_session: Session
    ):
        orm_id = getattr(cls.orm_table, cls.primary_key_col)
        try:
            db_session.query(cls.orm_table).filter(orm_id == resource_id).update(  # type: ignore
                jsonable_encoder(change_set)
            )
            commit(session=db_session)
        except sqlalchemy.exc.IntegrityError as e:
            logger.warning(e)
            #TODO : Raise Custom Exceptions
            raise Exception()

    @classmethod
    def delete(cls, *, resource_id: I, db_session: Session) -> None:
        orm_id = getattr(cls.orm_table, cls.primary_key_col)

        # TODO catch DNE
        db_session.query(cls.orm_table).filter(
            orm_id == resource_id
        ).delete()  # type: ignore

    @classmethod
    def count(
        cls,
        *,
        db_session: Session,
        filters: Filters = (),
    ) -> int:
        q: Query = typing.cast(Query, db_session.query(cls.orm_table).filter(*filters))

        return q.count()
