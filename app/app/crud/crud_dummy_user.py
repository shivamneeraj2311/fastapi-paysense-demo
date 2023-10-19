from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.dummy_user import  DummyUser
from app.schemas.dummy_user import DummyUserCreate, DummyUserUpdate

class CRUDDummyUser(CRUDBase[DummyUser, DummyUserCreate, DummyUserUpdate]):
    pass

dummy_user = CRUDDummyUser(DummyUser)

