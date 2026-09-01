from datetime import datetime,timezone
from pydantic import BaseModel,EmailStr,Field

class UserCreate(BaseModel):
    email: EmailStr
    password:str

class UserOut(BaseModel):
    id : int
    email : EmailStr
    role: str
    created_At = datetime
    updated_At = datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token : str
    token_type:str = Field(default="bearer")
    user_id : int
    role:str
    email:EmailStr