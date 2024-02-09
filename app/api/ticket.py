from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session

from app.repo import ticket_repo
from app.dependencies.db import get_db
from app.schemas.schema import BookTicketSchema , BookTicketResponseSchema

ticket_router = APIRouter(
    prefix="/ticket",
    tags=['ticket'],
)

@ticket_router.post("/book_ticket",status_code=200,response_model=BookTicketResponseSchema)
async def book_ticket(request : BookTicketSchema, db : Session = Depends(get_db)):
    return ticket_repo.book_ticket(request , db)

