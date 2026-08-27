from pydantic import BaseModel , EmailStr , Field , computed_field
from typing import Optional, Annotated


class Patient(BaseModel):
    name: str
    email:EmailStr
    age:Optional[int] = Field(default=None , gt=0)
    weight :float
    height :float
    married:bool = False
    allergies:list[str]
    contact_details : dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float :
        bmi = round(self.weight/(self.height**2) , 2)
        return bmi


    



def print_patient(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.bmi)


patient_info = {
    "name" : "Vishal",
    "email": "vis12h@hdfc.com",
    "age" : 90 ,
    "weight" : 50.4 ,
    'height' : 1.60,
    "allergies" : ['g' , 'B' ,'C' , 'D'],
    'contact_details' : {
        'emergency' : '98329092',
        'time' :'2333404'
    }

}

print_patient(Patient(**patient_info))
