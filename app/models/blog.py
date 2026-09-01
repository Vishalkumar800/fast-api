from pydantic import BaseModel
from sqlalchemy import Column , Integer, String, DateTime,Text , ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime , timezone

class Blog(BaseModel):

    __tablename__ = "blogs"
    id = Column(Integer , primary_key=True , index=True)
    title =  Column(String,index=True)
    slug = Column(String , index=True ,unique=True)
    content = Column(Text)
    author_id = Column(Integer , ForeignKey('users.id'))
    created_At = Column(DateTime , default= lambda: datetime.now(timezone.utc))
    updated_At = Column(DateTime , default=lambda:datetime.now(timezone.utc))

    author = relationship("User" , back_populates="blogs")

    def __repr__(self) -> str:
        return f"User(title = {self.title} , slug = '{self.slug})"

