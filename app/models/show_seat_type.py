from sqlalchemy import Column, Integer, ForeignKey, Enum

import enum
from app.dependencies.db import Base


class SeatType(enum.Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"


class ShowSeatType(Base):
    __tablename__ = "showseattype"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    show_id = Column(Integer, ForeignKey("show.id", ondelete="CASCADE"))
    seat_type = Column(Enum(SeatType))
    price = Column(
        Integer,
    )
