from pydantic import BaseModel , EmailStr , Field , field_validator ,model_validator
from typing import Optional, Annotated


class Patient(BaseModel):
    name: str
    email:EmailStr
    age:Optional[int] = Field(default=None , gt=0)
    weight :float
    married:bool = False
    allergies:list[str]
    contact_details : dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com' , 'icici.com']

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

        return value

    @model_validator(mode='after') #type coercein ke baad 
    def validate_emergency_details(cls, model):

        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Emergency Contact details required for patient whose age is greater than 60')
        return model




def print_patient(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)


patient_info = {
    "name" : "Vishal",
    "email": "vis12h@hdfc.com",
    "age" : 90 ,
    "weight" : 20.4 ,
    "allergies" : ['g' , 'B' ,'C' , 'D'],
    'contact_details' : {
        'emergency' : '98329092',
        'time' :'2333404'
    }

}

print_patient(Patient(**patient_info))
