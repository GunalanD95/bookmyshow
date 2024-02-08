from fastapi import FastAPI


from app.dependencies.db import engine
from app.models.base import Base
from app.api.ticket import ticket_router

from app.seed_data import seed_data_function

# app instance
app = FastAPI()


# Create tables
Base.metadata.create_all(bind=engine)


# register the routes here
app.include_router(ticket_router)


@app.get("/")
def index():
    return 'Welcome to BookMyShow'


def seed_data_on_startup():
    seed_data_function()  

# loaded dummy data to db
# @app.on_event("startup")
# async def startup_event():
#     seed_data_on_startup()



