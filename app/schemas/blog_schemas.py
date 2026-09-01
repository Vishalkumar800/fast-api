from pydantic import BaseModel , Field
from datetime import datetime
from typing import Optional

class BlogCreate(BaseModel):
    title : str  = Field(... , min_length=1 , max_length=100)
    content : str = Field(... , min_length=1 ) # three dot means field importnat hai aana hi chahiye

class BlogOut(BaseModel):
    id : int
    title : str
    slug : str
    content : str
    author_id : str
    created_At : datetime
    updated_At : datetime

    class Config:
        from_attributes = True

class PaginationParmas(BaseModel):
    page: Optional[int] = Field(1 , ge=1)
        

"""
class Config ka main kaam Pydantic ko batana hai ki data kis tarah read karna hai.

from_attributes = True kya karta hai?
Ye Pydantic ko allow karta hai ki woh object ke attributes se data read karke Pydantic model bana sake.

simple : pdynatic form me database se value utaoo

"""