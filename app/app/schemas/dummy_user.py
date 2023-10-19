from typing import Optional
from pydantic import BaseModel

class DummyUserBase(BaseModel):
    dummy_name: Optional[str] = None
    dummy_surname: Optional[str] = None


# Properties to receive on item creation
class DummyUserCreate(DummyUserBase):
    dummy_name: str
    dummy_surname: str


# Properties to receive on item update
class DummyUserUpdate(DummyUserCreate):
    pass


# Properties shared by models stored in DB
class DummyUserInDBBase(DummyUserBase):
    id: int
    dummy_name: str
    dummy_surname: str

    class Config:
        orm_mode = True


# Properties to return to client
class DummyUser(DummyUserInDBBase):
    pass


# Properties properties stored in DB
class DummyUserInDB(DummyUserInDBBase):
    pass

