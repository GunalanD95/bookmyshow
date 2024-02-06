from app.dependencies.db import Base
from sqlalchemy import Column, Integer

class BaseModel(Base):
    __tablename__ = 'basemodel'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, server_default='AUTO_INCREMENT()')
