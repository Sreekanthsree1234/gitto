from sqlalchemy import Column,Integer,String
from sqlalchemy import Enum as SQLEnum
from enum import Enum as PyEnum
from database import Base

class UserRole(str,PyEnum):
    MANAGER = "MANAGER"
    EMPLOYEE = "EMPLOYEE"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key = True,index = True)
    username = Column(String(255),unique = True,nullable = False)
    password_hash = Column(String(255),nullable = False)
    role = Column(SQLEnum(UserRole),nullable = False)