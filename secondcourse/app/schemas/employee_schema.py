from pydantic import BaseModel , Field , EmailStr
from typing import Optional

class EmployeeRequest(BaseModel):
    name: str = Field(..., min_length=3 , max_length=100)
    email : EmailStr
    department : str = Field(... , min_length=3)
    salary: float = Field(..., gt=0)

class EmployeeResponse(BaseModel):
    id:int
    name:str
    email:str