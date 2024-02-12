from sqlalchemy import Column, Integer, Sequence, DateTime, ForeignKey, Enum, Table

import enum
from sqlalchemy.orm import relationship
from app.dependencies.db import Base


class TicketStatus(enum.Enum):
    BOOKED = "booked"
    CANCELLED = "cancelled"
    PENDING = "pending"
    AVAIALABLE = "available"


ticket_show_seat_association = Table(
    "ticket_show_seat_association",
    Base.metadata,
    Column("ticket_id", Integer, ForeignKey("ticket.id")),
    Column("showseat_id", Integer, ForeignKey("showseat.id")),
)


class Ticket(Base):
    __tablename__ = "ticket"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ticket_id = Column(
        Integer(), Sequence("ticket_id_seq", start=1000), index=True, autoincrement=True
    )
    booking_time = Column(DateTime())
    show_id = Column(Integer, ForeignKey("show.id", ondelete="CASCADE"))
    booked_by = Column(Integer, ForeignKey("user.id"))
    ticket_status = Column(Enum(TicketStatus), default=TicketStatus.AVAIALABLE)

    # reason for many to many is cancelled tickets
    show_seats = relationship("ShowSeat", secondary=ticket_show_seat_association)
