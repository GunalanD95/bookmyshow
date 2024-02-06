from sqlalchemy import Column, Integer, ForeignKey, Enum

import enum
from app.dependencies.db import Base


class SeatStatus(enum.Enum):
    AVAILABLE = 'available'
    BOOKED = 'booked'
    LOCKED = 'locked'
    CANCELLED = 'cancelled'

class ShowSeat(Base):
    __tablename__ = 'showseat'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    show_id = Column(Integer, ForeignKey('show.id', ondelete='CASCADE'))
    seat_id = Column(Integer, ForeignKey('seat.id', ondelete='CASCADE'))
    show_seat_type = Column(Integer, ForeignKey('showseattype.id', ondelete='CASCADE'))
    status = Column(Enum(SeatStatus), default=SeatStatus.AVAILABLE)
