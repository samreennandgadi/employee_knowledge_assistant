from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import Employee
from backend.schemas import EmployeeCreate, EmployeeResponse


router = APIRouter(
    prefix="/employees",
    tags=["Employees"],
)


@router.post(
    "",
    response_model=EmployeeResponse,
    status_code=201,
)
def create_employee(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db),
):
    existing = (
        db.query(Employee)
        .filter(Employee.email == employee_data.email)
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=409,
            detail="Employee already exists",
        )

    employee = Employee(
        employee_code=employee_data.employee_code,
        name=employee_data.name,
        email=employee_data.email,
        job_title=employee_data.job_title,
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee


@router.get(
    "",
    response_model=list[EmployeeResponse],
)
def get_employees(
    db: Session = Depends(get_db),
):
    return db.query(Employee).all()
