import typing

import pydantic.networks
import shortuuid
from pydantic.validators import str_validator


from src.models.id_prefix import IdPrefix

T = typing.TypeVar("T", bound="IdStr")


class IdStr(str):
    prefix: str = IdPrefix.NONE
    random: bool = False
    random_length: int = 22

    @classmethod
    def __modify_schema__(cls, field_schema: typing.Dict[str, typing.Any]) -> None:
        field_schema.update(type="string", format="id")

    @classmethod
    def __get_validators__(cls) -> "pydantic.networks.CallableGenerator":
        yield str_validator
        yield cls.validate

    @classmethod
    def validate(cls, value: typing.Union[str, "IdStr"]) -> str:
        true_prefix = (
            cls.prefix if cls.prefix is IdPrefix.NONE else f"{cls.prefix[:10]}_"
        )

        if not value.startswith(true_prefix):
            raise ValueError(
                f"invalid id: {value} -- {cls.__name__} must start with prefix '{true_prefix}'"
            )
        return value

    @classmethod
    def make(cls: typing.Type[T]) -> T:
        if cls.random:
            return cls(make_random_id(cls.prefix, cls.random_length))

        return cls(make_named_uuid(cls.prefix))

    def __hash__(self) -> int:
        return super().__hash__()


def make_random_id(name: str, length: int = 22):
    rid: str = shortuuid.random(length)

    return f"{name[:10]}_{rid}"


def make_named_uuid(name: str):
    suuid: str = shortuuid.uuid()
    # TODO check if max length is 33 (10 + 1 + 22) and change id len in schema to 33 depending on this
    return f"{name[:10]}_{suuid}"  # max 36


def make_short_id() -> str:
    short_id = shortuuid.uuid()[:8].upper()
    return short_id
