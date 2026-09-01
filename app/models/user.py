from sqlalchemy import Column , Integer ,String , DateTime
from sqlalchemy.orm import relationship
from datetime import datetime , timezone
from app.database.base import Base


class User(Base):

    __tablename__ = "users"
    id = Column(Integer , primary_key=True , index=True)
    email = Column(String(255) , nullable= False , unique=True, index=True)
    password = Column(String(255), nullable=False)
    role = Column(String(50) , default='user')
    created_At =Column(DateTime , default= lambda: datetime.now(timezone.utc)) # Note here DateTime is datatype like string int etc
    updated_At = Column(DateTime ,default= lambda: datetime.now(timezone.utc) , onupdate=lambda: datetime.now(timezone.utc))
    # function ko abhi nahi, zarurat padne par chalana you can search on internet or chatgpt
    #Relationship 
    blogs = relationship("Blog" , back_populates='author' , cascade='all, delete-orphan')

    def __repr__(self) -> str:

        return f"User(id={self.id}, email={self.email}, role={self.role})"









