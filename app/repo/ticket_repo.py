
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from datetime import datetime


from app.models.show_seat import SeatStatus, ShowSeat
from app.models.ticket import Ticket , TicketStatus
from app.models.payment import Payment , PaymentType , PaymentStatus
from app.schemas.schema import BookTicketResponseSchema

def book_ticket(request, db):
    # booking logic
    # 1-> search the show seat ids in database
    # 2-> check if seat is available
       # if not available -> raise an exception
    # 4-> update the seat status ( hanling concurrency issue )
    # 5-> make a payment
    # 6-> book the ticket and return the ticket id  
      
    # Start a transaction
   with db.begin():
      show_seat_ids_db = db.query(ShowSeat).filter(ShowSeat.id.in_(request.show_seat_ids)).all()

      if not show_seat_ids_db:
         return HTTPException(status_code=404, detail="Invalid Show Seat Ids")

      for show_seat in show_seat_ids_db:
         if show_seat.status != SeatStatus.AVAILABLE:
            return HTTPException(status_code=404, detail="Show Seat Is Not Available")

      for show_seat in show_seat_ids_db:
         show_seat.status = SeatStatus.LOCKED
         db.add(show_seat)

      # Create ticket
      ticket = Ticket(
         booking_time=datetime.now(),
         show_id=request.show_id,
         booked_by=request.user_id,
         ticket_status=TicketStatus.BOOKED,
      )

      ticket.show_seats.extend(show_seat_ids_db)
      db.add(ticket)

      # Create payment
      payment = Payment(
         payment_type=PaymentType.CASH,
         payment_status=PaymentStatus.PENDING,
         ticket_id=ticket.id,
         amount=request.ticket_amount,
      )

      payment.payment_status = PaymentStatus.PAID
      db.add(payment)
      
      
   db.commit()
   
   response = BookTicketResponseSchema(
      ticket_id=ticket.id,
      booking_time= str(ticket.booking_time) ,
      show_id=ticket.show_id,
      ticket_status=ticket.ticket_status
   )

   return response