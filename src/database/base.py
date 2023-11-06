from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import as_declarative, declared_attr, declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

#TODO: check why auto update is not working on updatec_date
@as_declarative()
class Base:
    id =  Column(Integer, primary_key=True, index=True)
    created_date =  Column(DateTime(timezone=True), nullable=False)
    updated_date = Column(DateTime(timezone=True), nullable=False, onupdate=func.now())
    __name__: str
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__  # type: ignore