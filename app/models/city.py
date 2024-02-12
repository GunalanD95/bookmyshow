from sqlalchemy import Column, String, Integer

from app.dependencies.db import Base


class City(Base):
    __tablename__ = "city"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=True, unique=True)
