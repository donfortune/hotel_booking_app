import pandas as pd

data = pd.read_csv('hotels.csv', dtype={'id': str}) #make sure your string type 'id' is treated as a string not int

class User:
    def view_hotel(self):
        pass

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = data.loc[data['id'] == self.hotel_id, "name"].squeeze()
        self.city = data.loc[data['id'] == self.hotel_id, "city"].squeeze()


    def available(self):    #checks if there are free rooms in the hotel 
        availability = data.loc[data['id'] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False
        

    def book(self):   #books rooms by changing availability to no
        availability = data.loc[data['id'] == self.hotel_id, "available"].squeeze()
        if availability == "no":
            data.to_csv('hotels.csv', index=False)
        #data.loc[data['id'] == self.hotel_id, "available"] = 'no' 
        #data.to_csv('hotels.csv', index=False)
        

class ReservationTicket:
    def __init__(self, client_name, hotel_obj, city):
        self.client_name = client_name
        self.hotel = hotel_obj
        self.city = city


    def get_reserve_ticket(self):
       content = f"Mr {self.client_name} has booked {self.hotel.name}  in  {self.city} city successfully"
       return content

print(data)

hotel_ID = input('Enter Id of hotel:')
hotel = Hotel(hotel_ID)
if hotel.available():
    hotel.book()
    name = input('Enter your name:')
    reservation_ticket = ReservationTicket(client_name=name, hotel_obj=hotel, city=city)
    print(reservation_ticket.get_reserve_ticket())
    
else:
    print('Hotel is fully Booked')
    
    


