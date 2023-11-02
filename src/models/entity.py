import pydantic
class Entity(pydantic.BaseModel):
    class Config:
        orm_mode = True
        extra = "forbid"
