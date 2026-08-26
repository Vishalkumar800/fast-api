from pydantic import BaseModel
from typing import Optional

class Patient(BaseModel):

    name : str
    age :int = 20
    singer:bool = False # agr kuch nhi doge toh false aayega 
    weight : float
    married:Optional[bool] = None
    allergies : list[str]
    contact_details : dict[str,str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.singer)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

patient_info = {
    "name" : "Vishal",
    "age" : 30 ,
    "weight" : 20.4 ,
    "allergies" : ['g' , 'B' ,'C' , 'D'],
    "contact_details" : {
        "phone" : "96721823",
        "eamil" : "asgjdsh@gmail.com"
    }

}

patient = Patient(**patient_info)
insert_patient_data(patient=patient)