from pydantic import BaseModel , Field , EmailStr
from typing import Optional

class EmployeeRequest(BaseModel):
    name: str = Field(..., min_length=3 , max_length=100)
    email : EmailStr
    department : str = Field(... , min_length=2)
    salary: float = Field(..., gt=0)
    roll:str = Field(... , min_length=2)

class EmployeeResponse(BaseModel):
    id:int
    name:str
    email:str

class EmployeeUpdateRequest(BaseModel):
    name: Optional[str] = Field(None, min_length=3 , max_length = 100)
    email:Optional[EmailStr] = None
    department:Optional[str] = Field(None, min_length=2)
    salary:Optional[float] = Field(None ,gt= 0)
    roll: Optional[str] = Field(None, min_length=2)
