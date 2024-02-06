from pydantic import BaseModel 
from typing   import List 

class BookTicketSchema(BaseModel):
    show_ids: List[int]