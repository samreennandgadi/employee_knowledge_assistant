from pydantic import BaseModel, EmailStr, ConfigDict


class EmployeeCreate(BaseModel):
    employee_code: str
    name: str
    email: EmailStr
    job_title: str


class EmployeeResponse(BaseModel):
    id: int
    employee_code: str
    name: str
    email: EmailStr
    job_title: str

    model_config = ConfigDict(from_attributes=True)
