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

## Sorting

SORT_FIELDS = ["marks","age","name"]
SORT_ORDER = ["asc","desc"]

@app.get("/sort")
def student_sort(
    sorted_by:str = Query(None, description="Herre you can age ,marks and course"),
    order:str = Query("asc", description="Order like asc or desc" , examples=["asc"])
    ):

    if sorted_by not in SORT_FIELDS:
        raise HTTPException(
            status_code=404, 
            detail=f"Invalid sorted by '{sorted_by} Choose From {SORT_FIELDS}'"
            )

    if order not in SORT_ORDER:
        raise HTTPException(
            status_code=404,
            detail= f"Invalid order {order} Choose From {SORT_ORDER}"
        )

    data = get_data()

    students = []

    for student_id, info in data.items():
        info["id"] = student_id
        students.append(info)

    reverse = (order=="desc")

    sorted_student = sorted(students,key=lambda s:s[sorted_by] , reverse=reverse)
    return sorted_student
    



    
