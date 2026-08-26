from pydantic import BaseModel

class User(BaseModel):
    name: str
    age:int

patient_info = {"name":"Vishal" , "age":20}

# Note :
# patient_info = {"name":"Vishal" , "age":'20'} yha pydantic apne aap 20 str ko int me convert kr dega 

def printUser(user:User):
    print(user.name)
    print(user.age)

patient = User(**patient_info)

printUser(patient)