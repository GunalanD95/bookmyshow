from sqlalchemy import Column, Integer,  ForeignKey , Enum , Float

import enum
from sqlalchemy.orm import relationship
from app.dependencies.db import Base

class PaymentType(enum.Enum):
    CASH = 'cash'
    ONLINE = 'online'
    CARD   = 'card'
    
class PaymentStatus(enum.Enum):
    PENDING  = 'pending'
    PAID   = 'paid'
    FAILED = 'failed'
    

class Payment(Base):
    __tablename__ = 'payment'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    payment_type = Column(Enum(PaymentType))
    payment_status = Column(Enum(PaymentStatus))
    ticket_id = Column(Integer,ForeignKey('ticket.id'))
    reference_id = Column(Integer()) # 3rd party apps
    amount = Column(Float())
    
    