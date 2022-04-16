from sqlalchemy import Column, Integer, Date, Boolean
from sqlalchemy.orm import relationship

from backend.app.db.base_class import Base


class Schedule(Base):
    id = Column(Integer, primary_key=True)
    day = Column(Date, index=True, nullable=False)
    day_off = Column(Boolean(), default=False)
    employee = relationship("Schedule_Employee")
