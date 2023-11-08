from src.database.base import Base
from sqlalchemy import String, ForeignKey
from sqlalchemy import Column
from sqlalchemy.orm import relationship

metadata = Base.metadata


class User(Base):
    name = Column(String, index=True)
    surname = Column(String, index=True)


class Org(Base):
    dummy_user_id = Column(ForeignKey("User.id"), nullable=True, index=True)
    org_name = Column(String, index=True)
    dummy_user = relationship("User")
