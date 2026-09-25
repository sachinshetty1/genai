from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Employee structure
class Employee(BaseModel):
    id: int
    name: str
    age: int
    salary: float

# Collection for storing employees
employees = []          # id , name , age  , Salary , Designation 

# 1. CREATE - Add employee   as soon as we run 8000 very first emply url will load 
@app.get("/")
def home_employee():
    return {"message": "Welcome to EMployee Management Application "}

# 1. CREATE - Add employee
@app.post("/addEmployee")
def add_employee(employee: Employee):
    employees.append(employee)                  #  using append we are adding to list  

    return {
        "message": "Employee added successfully",
        "employee": employee
    }
    
# 2. READ - View all employees
@app.get("/allEmployees")
def get_all_employees():
    return employees


# 3. READ - Get employee by ID
@app.get("/employee/{employee_id}")
def get_employee(eid: int):

    for employee in employees:
        if employee.id == eid:
            return employee

    return {"message": "Employee not found"}

# 5. DELETE - Delete employee by ID
@app.delete("/deleteEmployee/{employee_id}")
def delete_employee(eid: int):

    for employee in employees:
        if employee.id == eid:
            employees.remove(employee)                      #  using remove we deleting the one  records from list  

            return {"message": "Employee deleted successfully"}

    return {"message": "Employee not found"}


# 6. DELETE - Delete all employees
@app.delete("/deleteAllEmployees")
def delete_all_employees():
    employees.clear()                                       #  using CLEAR  we deleting the ALL  records from list

    return {"message": "All employees deleted successfully"}



@app.put("/updateEmployee/{employee_id}")
def update_employee(eid: int, updatedvalues: Employee):
    for employee in employees:
        if employee.id == eid:
            # Update only these fields
            employee.name = updatedvalues.name
            employee.age = updatedvalues.age
            employee.salary = updatedvalues.salary
            
            return {
                "message": "Employee updated successfully",
                "employee": employee
            }

    return {"message": "Employee not found"}