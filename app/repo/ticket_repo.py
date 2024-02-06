
from fastapi import HTTPException

def book_ticket(request, db):
    raise HTTPException(status_code=200, detail="Booked Successfully")