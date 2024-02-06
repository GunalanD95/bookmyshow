from sqlalchemy import Column, Integer, String , ForeignKey , Enum

import enum
from app.dependencies.db import Base

class SeatStatusEnum(enum.Enum):
    AVAILABLE = 'available'
    BOOKED    = 'booked'
    RESERVED  = 'reserved'

class Seat(Base):
    __tablename__ = 'seat'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name        = Column(String(255))
    seat_num    = Column(Integer())
    row = Column(Integer())
    col = Column(Integer())
    seat_status = Column(Enum(SeatStatusEnum), default=SeatStatusEnum.AVAILABLE)
    auditorium_id = Column(Integer ,ForeignKey('auditorium.id',ondelete='CASCADE'))

