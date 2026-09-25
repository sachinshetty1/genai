from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/entry")
def entrypage():
    return {"message": "This is the entry page"}

@app.get("/employees")
def get_employees():
    return {
        "employees": [
            {"id": 1, "name": "Rahul", "salary": 45000},
            {"id": 2, "name": "Priya", "salary": 55000}
        ]
    }
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {
        "employee_id": employee_id
    }

class Employee(BaseModel):
    name: str
    email: str
    salary: float
    
@app.post("/employees")
def create_employee(employee: Employee):
    return {
        "message": "Employee created successfully",
        "employee": employee
    }
    
    
@app.put("/employees/{employee_id}")
def update_employee(employee_id: int, employee: Employee):
    return {
        "message": "Employee updated successfully",
        "employee_id": employee_id,
        "employee": employee
    }
    

@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):
    return {
        "message": "Employee deleted successfully",
        "employee_id": employee_id
    }
    
