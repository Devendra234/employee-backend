from pydantic import BaseModel, EmailStr
from typing import Optional

class EmployeeCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str
    department: str
    designation: str
    salary: float
    status: str = "Active"


class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        from_attributes = True