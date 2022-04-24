from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Schedule_Employee(Base):
    schedule_id = Column(Integer, ForeignKey('schedule.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)
    shift = Column(Integer, nullable=False)
    schedule = relationship("Schedule", back_populates="employee")
    employee = relationship("Employee", back_populates="schedule")
