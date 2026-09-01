from fastapi import FastAPI
from testdata import employees
from pydantic import BaseModel

app = FastAPI()

class ResponseModelClass(BaseModel):
    id: int
    name: str
    age: int
    department: str
    salary: float

@app.get("/", response_model=list[ResponseModelClass])
def home():
    return employees



