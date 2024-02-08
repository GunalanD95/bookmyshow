
from fastapi import HTTPException
from app.models.show_seat import SeatStatus, ShowSeat

def book_ticket(request, db):
    # booking logic
    # 1-> search the show seat ids in database
    # 2-> check if seat is available
       # if not available -> raise an exception
    # 4-> update the seat status ( hanling concurrency issue )
    # 5-> make a payment
    # 6-> book the ticket and return the ticket id
   show_seat_ids = request.show_seat_ids
   user_id  = request.user_id
    
   for show_seat_id in show_seat_ids:
      seat = db.query(ShowSeat).filter(ShowSeat.id == show_seat_id).first()
      
      print('SEAT-->', seat)
      if seat and seat.status == SeatStatus.AVAILABLE:
         seat.status = SeatStatus.BOOKED
      else:
         raise HTTPException(status_code=400, detail="Seat is not available")
     
   db.commit()  
    