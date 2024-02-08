from pydantic import BaseModel 
from typing   import List 

class BookTicketSchema(BaseModel):
    show_seat_ids: List[int]
    user_id : int
