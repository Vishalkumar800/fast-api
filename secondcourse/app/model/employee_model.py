from pydantic import BaseModel
from sqlalchemy import Column , Integer , String
from secondcourse.app.database.base import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True , index=True)
    name= Column(String )
    email = Column(String , unique=True, index=True)
    department = Column(String)
    salary = Column(Integer)
    
    