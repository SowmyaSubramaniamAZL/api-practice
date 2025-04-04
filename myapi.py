# import the fastAPI as an object and import Path
from fastapi import FastAPI, Path

# import optional to use for query parameters 
from typing import Optional 

# pydantic - data validation and parsing library that ensures input data is structured correctly 
# BaseModel - used to define models with type validation, ensures that incoming data matches the expected format 
from pydantic import BaseModel

# create an instance of the FastAPI object 
app = FastAPI()

# endpoints:
# GET - get information or return information
# POST - create something new 
# PUT - update existing data in a particular object 
# DELETE - deleting something 

students = {
    1: {
        "name": "john", 
        "age": 17, 
        "year" : "year 12"
    }
}

# create an endpoint 
@app.get("/")
def index():
    return {"name": "First Data"}

# path parameter: dynamic input from the user that gets a specific data point based on the id. required and used to identify a specific resource. 
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    return students[student_id]

# query parameter: optional and used for filtering, sorting, etc. 
@app.get("/get-by-name/{student_id}")
def get_student(*, student_id: int, test:int, name: Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    
    return {"Data": "Not found"}

# defines a structured model for Student data 
class Student(BaseModel):
    name: str
    age: int
    year: str


# create a POST method 
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]


# define a model for updating student data
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# PUT method: 
@app.put("/update-student/{student-id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    # use 3 separate if statements so that only the fields that the user provided are updated and the other values aren't wiped out 
    if student.name is not None:
        students[student_id]["name"] = student.name
    if student.age is not None:
        students[student_id]["age"] = student.age
    if student.year is not None:
        students[student_id]["year"] = student.year

    return students[student_id]

# DELETE method:
@app.delete("/delete-student/{student-id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    
    del students[student_id]
    return {"Message": "Student deleted successfully."}