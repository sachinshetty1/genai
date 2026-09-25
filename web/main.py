from typing import Generator

from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import String, Float, create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    Session,
    mapped_column,
    sessionmaker
)


# =========================================================
# 1. DATABASE CONFIGURATION
# =========================================================

DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password="root",          # Change to your MySQL password
    host="localhost",
    port=3306,
    database="employee_db"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# =========================================================
# 2. BASE CLASS
# =========================================================

class Base(DeclarativeBase):
    pass


# =========================================================
# 3. DATABASE MODEL
# =========================================================

class Employee(Base):
    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    age: Mapped[int] = mapped_column(nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=False)
    designation: Mapped[str] = mapped_column(String(100), nullable=False)


# Create the table if it does not exist
Base.metadata.create_all(bind=engine)


# =========================================================
# 4. PYDANTIC SCHEMAS
# =========================================================

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    age: int = Field(ge=18, le=60)
    salary: float = Field(gt=0)
    designation: str = Field(min_length=2, max_length=100)


class EmployeeUpdate(BaseModel):
    name: str = Field(min_length=3, max_length=100)
    age: int = Field(ge=18, le=60)
    salary: float = Field(gt=0)
    designation: str = Field(min_length=2, max_length=100)


class EmployeeResponse(BaseModel):
    id: int
    name: str
    age: int
    salary: float
    designation: str

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# 5. DATABASE SESSION
# =========================================================

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()


# =========================================================
# 6. FASTAPI APPLICATION
# =========================================================

app = FastAPI(
    title="Employee Management API",
    description="FastAPI CRUD application using MySQL",
    version="1.0.0"
)


# =========================================================
# 7. BASIC ENDPOINT
# =========================================================

@app.get("/")
def home():
    return {
        "message": "FastAPI with MySQL is working"
    }


# =========================================================
# 8. CREATE EMPLOYEE
# =========================================================

@app.post(
    "/employees",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED
)
def create_employee(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db)
):
    employee = Employee(
        name=employee_data.name,
        age=employee_data.age,
        salary=employee_data.salary,
        designation=employee_data.designation
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


# =========================================================
# 9. GET ALL EMPLOYEES
# =========================================================

@app.get(
    "/employees",
    response_model=list[EmployeeResponse]
)
def get_all_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return employees


# =========================================================
# 10. GET EMPLOYEE BY ID
# =========================================================

@app.get(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def get_employee_by_id(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found"
        )

    return employee


# =========================================================
# 11. UPDATE EMPLOYEE
# =========================================================

@app.put(
    "/employees/{employee_id}",
    response_model=EmployeeResponse
)
def update_employee(
    employee_id: int,
    employee_data: EmployeeUpdate,
    db: Session = Depends(get_db)
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found"
        )

    employee.name = employee_data.name
    employee.age = employee_data.age
    employee.salary = employee_data.salary
    employee.designation = employee_data.designation

    db.commit()
    db.refresh(employee)

    return employee


# =========================================================
# 12. DELETE EMPLOYEE
# =========================================================

@app.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    employee = db.get(Employee, employee_id)

    if employee is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with ID {employee_id} was not found"
        )

    db.delete(employee)
    db.commit()

    return {
        "message": f"Employee with ID {employee_id} deleted successfully"
    }


# =========================================================
# 13. DELETE ALL EMPLOYEES
# =========================================================

@app.delete("/employees")
def delete_all_employees(db: Session = Depends(get_db)):
    deleted_count = db.query(Employee).delete()
    db.commit()

    return {
        "message": "All employees deleted successfully",
        "deletedEmployees": deleted_count
    }