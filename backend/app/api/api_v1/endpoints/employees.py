from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app import schemas, crud
from app.api import deps
from app.core.security import get_password_hash

router = APIRouter()


@router.post("/create_employee", response_model=schemas.Employee)
def create_employee(
        *,
        db: Session = Depends(deps.get_db),
        employee_in: schemas.EmployeeCreate
) -> Any:
    """
    Create employee
    """
    employee = crud.employee.get_by_email(db=db, email=employee_in.email)
    if employee:
        raise HTTPException(
            status_code=400,
            detail="Email already in use"
        )
    return crud.employee.create(db=db, obj_in=employee_in)


@router.get("/get_employee_by_id/{id}", response_model=schemas.Employee)
def get_employee_by_id(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Get employee by id
    """
    return crud.employee.get(db=db, id=id)


@router.get("/get_employee_by_email/{email}", response_model=schemas.Employee)
def get_employee_by_email(
        *,
        db: Session = Depends(deps.get_db),
        email: str
) -> Any:
    """
    Get employee by email
    """
    return crud.employee.get_by_email(db=db, email=email)


@router.get("/get_employee_by_login/{login}", response_model=schemas.Employee)
def get_employee_by_login(
        *,
        db: Session = Depends(deps.get_db),
        login: str
) -> Any:
    """
    Get employee by login
    """
    return crud.employee.get_by_login(db=db, login=login)


@router.put("/create_account/{email}", response_model=schemas.Employee)
def create_account_by_email(
        *,
        db: Session = Depends(deps.get_db),
        email: str,
        login: str,
        password: str
) -> Any:
    """
    Create account for employee
    """
    employee = crud.employee.get_by_email(db=db, email=email)
    if not employee:
        raise HTTPException(
            status_code=404,
            detail="Employee with this email don't exist"
        )
    if employee.login:
        raise HTTPException(
            status_code=400,
            detail="Account already created"
        )
    employee_2 = crud.employee.get_by_login(db=db, login=login)
    if employee_2:
        raise HTTPException(
            status_code=400,
            detail="Login already in use"
        )
    employee_to_update = jsonable_encoder(employee)
    employee_updated = schemas.EmployeeUpdate(**employee_to_update)
    employee_updated.login = login
    employee_updated.password = get_password_hash(password=password)
    return crud.position.update(db=db, db_obj=employee, obj_in=employee_updated)

@router.delete("/delete_employee/{id}", response_model=schemas.Employee)
def delete_employee(
        *,
        db: Session = Depends(deps.get_db),
        id: int
) -> Any:
    """
    Delete an employee
    """
    return crud.employee.remove(db=db, id=id)
