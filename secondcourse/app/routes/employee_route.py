from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from secondcourse.app.database.session import get_db
from secondcourse.app.controllers.employee_controller import get_employee_controller
from secondcourse.app.schemas.employee_schema import EmployeeResponse

router = APIRouter()

@router.get("/employees/", response_model=list[EmployeeResponse])
def get_employees(db:Session = Depends(get_db)):
    return get_employee_controller(db)