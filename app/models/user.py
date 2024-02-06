from sqlalchemy import Column, Integer, String

from app.dependencies.db import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    email_id = Column(String(255), unique=True)  # Assuming email_id is intended for email addresses
