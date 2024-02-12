from pydantic import BaseModel
from typing import List


class BookTicketSchema(BaseModel):
    show_seat_ids: List[int]
    user_id: int
    show_id: int
    ticket_amount: int


class BookTicketResponseSchema(BaseModel):
    ticket_id: int
    booking_time: str
    show_id: int
    ticket_status: str
