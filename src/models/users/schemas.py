import datetime
from src.models import accessor as accessor
from src.database import orm
from typing import Optional
from pydantic import BaseModel
from src.models import entity
from src.models.id_prefix import IdPrefix
from src.models.id import IdStr
from src.common_utils.date_utils import get_utc_now


class UserID(IdStr):
    prefix = IdPrefix.DUMMY_USER


class UserDTO(BaseModel):
    name: Optional[str] = None
    surname: Optional[str] = None


# Properties to receive on item creation
class UserCreateDTO(UserDTO):
    name: str
    surname: str


# Properties to receive on item update
class UserUpdateDTO(UserCreateDTO):
    ...


# Properties shared by models stored in DB
class UserSerializer(entity.Entity):
    name: str
    surname: str
    created_date: datetime.datetime
    updated_date: datetime.datetime

    @classmethod
    def create(cls, *, name: str, surname: str):
        created_date = get_utc_now()
        updated_date = get_utc_now()
        name = name
        surname = surname

        return cls(
            name=name,
            created_date=created_date,
            surname=surname,
            updated_date=updated_date,
        )


# API Response Model
class UserResponseDTO(UserSerializer):
    pass


class UserAccessor(accessor.Accessor[orm.User, UserSerializer, orm.User.id]):
    orm_table = orm.User
    entity = UserSerializer
