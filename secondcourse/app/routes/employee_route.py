from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from secondcourse.app.database.session import get_db
from secondcourse.app.schemas.employee_schema import EmployeeRequest , EmployeeResponse , EmployeeUpdateRequest
from secondcourse.app.controllers.employee_controller import get_employee_controller , create_employee_controller , update_employee_controller, delete_employee_controller

router = APIRouter()

@router.get("/", response_model=list[EmployeeResponse])
def get_employees(db:Session = Depends(get_db)):
    return get_employee_controller(db)

@router.post("/")
def create_employee(employee_data:EmployeeRequest, db:Session = Depends(get_db)):
    return create_employee_controller(db , employee_data)

@router.patch("/{employee_id}")
def update_employee(employee_id:int , employee_data: EmployeeUpdateRequest ,db:Session = Depends(get_db) ):
    return update_employee_controller(db ,employee_id=employee_id , employee_data=employee_data)

@router.delete("/{employee_id}")
def delete_employee(employee_id:int , db:Session = Depends(get_db)):
    return delete_employee_controller(db , employee_id=employee_id)

'''
PUT   → Pura update
PATCH → Partial update

'''