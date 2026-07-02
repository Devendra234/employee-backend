from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import SessionLocal
from app.database.models import Employee
from app.schemas.employee import EmployeeCreate

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def add_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    new_employee = Employee(**employee.model_dump())

    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)

    return new_employee


@router.get("/")
def get_employees(db: Session = Depends(get_db)):
    return db.query(Employee).all()


@router.get("/{employee_id}")
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee


@router.put("/{employee_id}")
def update_employee(
    employee_id: int,
    employee: EmployeeCreate,
    db: Session = Depends(get_db),
):
    db_employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not db_employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    for key, value in employee.model_dump().items():
        setattr(db_employee, key, value)

    db.commit()
    db.refresh(db_employee)

    return db_employee


@router.delete("/{employee_id}")
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()

    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()

    return {"message": "Employee deleted successfully"}