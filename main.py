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
    def __init__(self, client_name, hotel_obj):
        self.client_name = client_name
        self.hotel = hotel_obj
       


    def get_reserve_ticket(self):
       content = f"""
                Thank you for your reservation!!
                Your Booking Details:
                Name : Mr {self.client_name}     
                Hotel :{self.hotel.name} 
                City : {self.hotel.city} 
                 """
       return content

class CreditCard:
    def __init__(self, card_number, expiration_date, holder_name, cvc):
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.holder_name = holder_name
        self.cvc = cvc
    
    def validate(self):
        if self.card_number.isdigit()  and self.expiration_date.isdigit() and self.cvc.isdigit() and self.holder_name:

            return True
        else:
            return False



        


print(data)

hotel_ID = input('Enter Id of hotel:')
hotel = Hotel(hotel_ID)
if hotel.available():
    card_number = input('enter your card number:')
    expiration_date = input('enter expiration date:')
    holder_name = input('Enter holders name:')
    cvc = input('Enter your cvc no:')
    credit_card = CreditCard(card_number, expiration_date, holder_name, cvc)
    if credit_card.validate():
        hotel.book()
        name = input('Enter your name:')
        reservation_ticket = ReservationTicket(client_name=name, hotel_obj=hotel)
        print(reservation_ticket.get_reserve_ticket())
    else:
        print('There was a problem with your card')
    
else:
    print('Hotel is fully Booked')
    
    


