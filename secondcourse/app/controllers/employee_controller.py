from secondcourse.app.services.employee_service import get_employee_service
from sqlalchemy.orm import Session

def get_employee_controller(db:Session):
    return get_employee_service(db)
   