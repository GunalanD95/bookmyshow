from sqlalchemy import Column, Integer, String, Table, ForeignKey, Enum
from sqlalchemy.orm import relationship

import enum
from app.dependencies.db import Base

# Association Table for Many-to-Many Relationship
# REF : https://medium.com/@warrenzhang17/many-to-many-relationships-in-sqlalchemy-ba08f8e9ccf7#:~:text=Setting%20Up%20Many%2Dto%2DMany%20Relationships%20in%20SQLAlchemy&text=Here%2C%20I've%20defined%20a,to%20denote%20the%20association%20table.
movie_actor_association = Table(
    "movie_actor_association",
    Base.metadata,
    Column("movie_id", Integer, ForeignKey("movie.id")),
    Column("actor_id", Integer, ForeignKey("actor.id")),
)


class Languages(enum.Enum):
    TAMIL = "tamil"
    ENGLISH = "english"
    HINDI = "hindi"


class Actor(Base):
    __tablename__ = "actor"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    movies = relationship(
        "Movie", secondary=movie_actor_association, back_populates="actors"
    )


class Movie(Base):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))
    auditorium_id = Column(Integer, ForeignKey("auditorium.id", ondelete="CASCADE"))
    actors = relationship(
        "Actor", secondary=movie_actor_association, back_populates="movies"
    )
    languages = Column(Enum(Languages))
