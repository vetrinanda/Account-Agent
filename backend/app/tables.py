from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    balance=Column(Integer,primary_key=True,index=True)
    nonlocalame = Column(String, index=True)
    email = Column(String, index=True)