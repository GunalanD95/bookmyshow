# creating and connecting the db with our FastApi App
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import URL



url_object = URL.create(
    "postgresql",
    username="postgres",
    password="admin@123",  
    host="localhost",
    database="bookmyshow",
)


engine = create_engine(url_object ,echo= True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# creates db session object for each request 
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close