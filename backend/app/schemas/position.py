from pydantic import BaseModel


class PositionBase(BaseModel):
    name: str


class PositionCreate(PositionBase):
    name: str


class PositionUpdate(PositionBase):
    pass


class PositionInDBBase(PositionBase):
    id: int
    name: str

    class Config:
        orm_mode = True


class Position(PositionInDBBase):
    pass


class PositionInDB(PositionInDBBase):
    pass
