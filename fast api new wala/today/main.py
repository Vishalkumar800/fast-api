from fastapi import FastAPI ,HTTPException,Query
import json

app = FastAPI()

@app.get("/")
def home():
    return {"Hello I am here"}

def get_data():
    with open("students.json","r") as file:
        return json.load(file)

@app.get("/students")
def students():
    return get_data()

@app.get("/students/{id}")
def get_student_ById(id:str):
    data = get_data()

    if id not in data:
        raise HTTPException(
            status_code=404,
            detail=f"Student with Id '{id}' not found"
            )

    return data[id]



@app.get("/filter")
def student_filter(course:str = Query(default=None , examples=["Python"])):

    data = get_data()

    filterItems = {}

    if course == None:
        return data

    for id , info in data.items():
        if info["course"].lower() == course.lower():
            filterItems[id] = info
    return filterItems

 

    
