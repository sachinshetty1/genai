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