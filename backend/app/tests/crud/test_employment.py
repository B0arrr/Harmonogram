import random

from sqlalchemy.orm import Session

from app import crud
from app.schemas import EmploymentCreate
from app.tests.utils.employment import create_random_employment
from app.tests.utils.utils import random_lower_string


def test_create_employment(db: Session):
    employment = random_lower_string()
    hours_per_day = random.randint(1, 10)
    hours_per_week = random.randint(1, 10)
    employment_in = EmploymentCreate(employment=employment,
                                     hours_per_week=hours_per_week,
                                     hours_per_day=hours_per_day)
    employment_new = crud.employment.create(db=db,
                                            obj_in=employment_in)
    assert employment_new
    assert employment_in
    assert employment_new.employment == employment_in.employment
    assert employment_new.hours_per_day == employment_in.hours_per_day
    assert employment_new.hours_per_week == employment_in.hours_per_week


def test_get_employment_by_id(db: Session):
    employment = create_random_employment(db=db)
    get_employment = crud.employment.get(db=db,
                                         id=employment.id)
    assert get_employment
    assert employment.id == get_employment.id
    assert employment.hours_per_week == get_employment.hours_per_week
    assert employment.hours_per_day == get_employment.hours_per_day


def test_employment_id(db: Session):
    employment = create_random_employment(db=db)
    get_employment = crud.employment.get_id(db=db,
                                            name=employment.employment)

    assert get_employment
    assert employment.id == get_employment
