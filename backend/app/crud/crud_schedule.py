import datetime
from typing import List

from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models import Schedule
from app.schemas.schedule import ScheduleUpdate, ScheduleCreate


class CRUDSchedule(CRUDBase[Schedule, ScheduleCreate, ScheduleUpdate]):
    def create_schedule(self, db: Session, *, day: datetime.date, day_off: bool) -> Schedule:
        schedule = Schedule(day=day, day_off=day_off)
        db.add(schedule)
        db.commit()
        db.refresh(schedule)
        return schedule

    def get_id(
            self, db: Session, *, day: datetime.date
    ) -> int:
        return db.query(self.model).filter(Schedule.day == day).first().id

    def get_day_by_id(
            self, db: Session, *, id: int
    ) -> str:
        return db.query(self.model).filter(Schedule.id == id).first().day

    def get_all(
            self, db: Session
    ) -> List[Schedule]:
        return db.query(self.model).all()

    def get_days(
            self, db: Session, *, start_date: datetime.date, end_date: datetime.date
    ) -> List[Schedule]:
        return db.query(self.model).filter(Schedule.day >= start_date, Schedule.day <= end_date).all()


schedule = CRUDSchedule(Schedule)
