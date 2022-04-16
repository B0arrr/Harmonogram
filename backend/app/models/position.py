from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from backend.app.db.base_class import Base


class Position(Base):
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    employee = relationship("Employee", ForeignKey("employee.id"))
