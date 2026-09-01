from secondcourse.app.model.employee_model import Employee
from sqlalchemy.orm import Session

def get_employee_service(db:Session):
    employee = db.query(Employee).all()
    return employee