from sqlalchemy import Column, Integer, String , ForeignKey

from app.dependencies.db import Base

class Theatre(Base):
    __tablename__ = 'theatre'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    city_id = Column(Integer ,ForeignKey('city.id',ondelete='CASCADE'))
    address = Column(String(255), nullable=True)