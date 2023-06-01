import pandas as pd

data = pd.read_csv('hotels.csv')

class User:
    def view_hotel(self):
        pass

class Hotel:
    def __init__(self, id):
        pass
    def available(self):
        pass
    def book(self):
        pass

class ReservationTicket:
    def __init__(self, client_name, hotel_obj):
        pass
    def get_reserve_ticket(self):
       pass

#print(data)

id = input('Enter Id of hotel:')
hotel = Hotel(id)
if hotel.available():
    hotel.book()
    name = input('Enter your name')
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.get_reserve_ticket())
else:
    print('Hotel is fully Booked')
    
    


