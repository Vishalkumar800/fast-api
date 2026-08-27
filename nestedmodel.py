from pydantic import BaseModel


class Address(BaseModel):
    village:str
    city:str
    pincode:int

class Patient(BaseModel):
    name:str
    age:int
    height:float
    address:Address

def print_patient(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.height)
    print(patient.address)

address_info = {
    'village' :'Gram Village',
    'city' : 'Gorakhpur',
    'pincode' : 273893
}

address = Address(**address_info)

patient_info = {
    'name':'Vishal',
    'age' : 80,
    'height' : 70.3,
    'address' : address
}

print_patient(
    patient=Patient(**patient_info)
)