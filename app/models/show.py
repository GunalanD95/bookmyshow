from sqlalchemy import Column, Integer, JSON, DateTime, ForeignKey

from app.dependencies.db import Base


class Show(Base):
    __tablename__ = "show"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    auditorium_id = Column(Integer, ForeignKey("auditorium.id", ondelete="CASCADE"))
    movie_id = Column(Integer, ForeignKey("movie.id"))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    show_features = Column(JSON)
