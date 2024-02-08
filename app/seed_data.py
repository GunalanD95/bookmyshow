
from sqlalchemy.orm import sessionmaker

from app.models.city import City
from app.models.theatre import Theatre
from app.models.auditorium import Auditorium
from app.models.movie import Movie , Actor , Languages
from app.models.show import Show
from app.models.seat import Seat , SeatStatusEnum
from app.models.show_seat import ShowSeat , SeatStatus
from app.models.show_seat_type import ShowSeatType , SeatType
from app.models.user import User 

from app.dependencies.db import engine



# Dummy data for Backend
def seed_data_function():
    Session = sessionmaker(engine)
    with Session() as session:

        # Add cities
        city1 = City(name='Chennai')
        city2 = City(name='Bangalore')
        
        session.add_all([city1, city2])
        session.commit()

        # Add theaters
        theater1 = Theatre(name='IMAX', city_id=city1.id)
        theater2 = Theatre(name='PVR',  city_id=city2.id)
        
        session.add_all([theater1, theater2])
        session.commit()    
        
        # Add Auditorium
        auditorium1 = Auditorium(name='IMAX Screen 1', theatre_id=theater1.id)
        auditorium2 = Auditorium(name='PVR Screen 1', theatre_id=theater2.id)
        session.add_all([auditorium1, auditorium2])
        session.commit()
            
        # Add Actors
        actor1 = Actor(name='Robert Downey Jr.')
        actor2 = Actor(name='Chris Hemsworth')
        session.add_all([actor1, actor2])
        session.commit()

        # Add Movie and its actors
        
        movie1 = Movie(name='Avengers', auditorium_id=auditorium1.id, languages=Languages.ENGLISH)
        movie1.actors.extend([actor1, actor2])
        
        movie2 = Movie(name='Thor', auditorium_id=auditorium2.id , languages=Languages.ENGLISH)
        movie2.actors.append(actor2)
        
        session.add_all([movie1, movie2])
        session.commit()
        
        
        # Add shows
        show1 = Show(auditorium_id=auditorium1.id, movie_id=movie1.id, start_time='2022-06-01 10:00:00', end_time='2022-06-01 12:00:00', show_features={'show_type': '2D'})
        show2 = Show(auditorium_id=auditorium2.id, movie_id=movie2.id, start_time='2022-06-01 10:00:00', end_time='2022-06-01 12:00:00', show_features={'show_type': '2D'})
        
        # Add seats , show_seat and show_seat_type
        seat_type = ShowSeatType(show_id=show1.id, seat_type=SeatType.BRONZE, price=100)
        seat_type_1 = ShowSeatType(show_id=show2.id, seat_type=SeatType.BRONZE, price=100)
        
        session.add_all([seat_type, seat_type_1])
        session.commit()
        
        
        for i in range(1, 11):
            for j in range(1, 11):
                seat1 = Seat(name=f'IMAX Screen Seat {i,j}', auditorium_id=auditorium1.id, seat_num=i*10+j, row=i, col=j, seat_status=SeatStatusEnum.AVAILABLE)
                seat2 = Seat(name=f'PVR Screen  Seat {i,j}', auditorium_id=auditorium2.id, seat_num=i*10+j, row=i, col=j, seat_status=SeatStatusEnum.AVAILABLE)

                session.add(seat1)
                session.add(seat2)

                show_seat = ShowSeat(show_id=show1.id, seat_id=seat1.id, show_seat_type=seat_type.id , status=SeatStatus.AVAILABLE)
                show_seat_1 = ShowSeat(show_id=show2.id, seat_id=seat2.id, show_seat_type=seat_type_1.id, status=SeatStatus.AVAILABLE)
                
                session.add_all([show_seat, show_seat_1])
                
                
        # Add User
        user1 = User(name='Vishal',email_id='vishal@123')
        user2 = User(name='Rohit',email_id='rohit@123')
        
        session.add_all([user1, user2])
        
        session.commit()