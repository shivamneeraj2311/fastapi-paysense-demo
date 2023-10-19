from sqlalchemy import Column, Integer, String, DateTime
from app.db.base_class import Base

class DummyUser(Base):
    id = Column(Integer, primary_key=True, index=True)
    dummy_name = Column(String, index=True)
    dummy_surname = Column(String, index=True)

