import random

from sqlalchemy.orm import Session

from app import crud
from app.schemas import EmploymentCreate
from app.tests.utils.utils import random_lower_string


def create_random_employment(db: Session):
    employment = random_lower_string()
    hours_per_day = random.randint(1, 10)
    hours_per_week = random.randint(1, 10)
    employment_in = EmploymentCreate(employment=employment,
                                     hours_per_week=hours_per_week,
                                     hours_per_day=hours_per_day)
    return crud.employment.create(db=db,
                                  obj_in=employment_in)
