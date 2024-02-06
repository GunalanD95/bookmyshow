from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from app.dependencies.db import Base

class Auditorium(Base):
    __tablename__ = 'auditorium'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    theatre_id = Column(Integer, ForeignKey('theatre.id', ondelete='CASCADE'))
    features = Column(JSON)
