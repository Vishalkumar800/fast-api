from secondcourse.app.model.employee_model import Employee
from sqlalchemy.orm import Session 
from fastapi import HTTPException, status

def get_employee_service(page:int , limit:int ,db:Session):
    skip = (page - 1) * limit
    employee = db.query(Employee).offset(skip).limit(limit).all()
    return employee


# Note alembic note me page and limit ki explanation hai agr bhul gye ho toh dekh lo ek bar 
'''
eske mtlb agr 10 offset ke andr pass kroge to 1st page ke 10 records skip ho jayenge aur 11th record se start hoga.
start me 0 hoga esliye 1st page ke liye (1-1)*10 = 0
2nd page ke liye (2-1)*10 = 10  

'''

def create_employee_service(db:Session , employee_data: dict):
    new_employee = Employee(**employee_data)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def update_employee_service(db:Session , employee_id:int , employee_data:dict):
    employee=  db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail= f"Employee with id{employee_id} not found")

    for key , value in employee_data.items():
        setattr(employee , key, value)

    db.commit()
    db.refresh(employee)
    return employee

def delete_employee_service(db:Session , employee_id:int):
    employee=  db.query(Employee).filter(Employee.id == employee_id).first()
    if not employee:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,detail=f"Employee with id{employee_id} not found")
    db.delete(employee)
    db.commit()
    return {"message": f"Employee with id {employee_id} deleted successfully."}


        


# Dynamic Object Update ⭐
# Multiple fields automatically update ho jayengi

"""
setattr() → attribute ki value SET / UPDATE
getattr() → attribute ki value GET
delattr() → attribute DELETE


"""

'''
exclude_unset=True important hai

Maan lo request:

{
  "salary": 50000
}

Normal:

employee_data.model_dump()

potentially optional fields ko bhi None ke saath dictionary me la sakta hai.

Lekin:

employee_data.model_dump(exclude_unset=True)

sirf user ne jo fields bheji hain wahi देगा:

{
    "salary": 50000
}

'''


