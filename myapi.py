# import the fastAPI as an object and import Path
from fastapi import FastAPI, Path

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
        "class" : "year 12"
    }
}

# create an endpoint 
@app.get("/")
def index():
    return {"name": "First Data"}

# path parameter: dynamic input from the user that gets a specific data point based on the id
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(..., description="The ID of the student you want to view", gt=0)):
    return students[student_id]

# query parameter: 
@app.get("/get-by-name")
def get_student(name: str):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    
    return {"Data": "Not found"}
