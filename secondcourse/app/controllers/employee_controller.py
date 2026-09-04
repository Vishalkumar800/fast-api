from secondcourse.app.services.employee_service import delete_employee_service, get_employee_service, create_employee_service , update_employee_service
from sqlalchemy.orm import Session

def get_employee_controller(db:Session):
    return get_employee_service(db)


def create_employee_controller(db:Session , employee_data):
    return create_employee_service(db , employee_data.model_dump())

def update_employee_controller(db:Session , employee_id:int , employee_data) :
    return update_employee_service(db , employee_id , employee_data.model_dump(exclude_unset = True) )

def delete_employee_controller(db:Session, employee_id:int):
    return delete_employee_service(db, employee_id)