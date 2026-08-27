from pydantic import BaseModel , EmailStr , Field
from typing import Optional

#AnyUrl 

''' Field 
me aap apne condition likh skhte ho ki koi minus value nhi daal skhta 

lt = lessthan
gt = greater than
ge = greater than equal to 
max_length = 50 (50 se jyda nhi chalega)

Annoted : 47:10

'''

class Patient(BaseModel):

    name : str
    age :int = 20
    email: EmailStr
    singer:bool = False # agr kuch nhi doge toh false aayega 
    weight : float = Field(gt=0) #greater than 0 chahiye hmesha *** (ge) means greater than equal to **
    married:Optional[bool] = None
    allergies : list[str]
    contact_details : dict[str,str]

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.email)
    print(patient.singer)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)

patient_info = {
    "name" : "Vishal",
    "email": "vis12h@gmail.com",
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