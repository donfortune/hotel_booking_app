import pandas

data = pandas.read_csv("hotels.csv", dtype={"id": str})
data_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
data_cards_security = pandas.read_csv("card-security.csv", dtype=str)

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = data.loc[data["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        
        data.loc[data["id"] == self.hotel_id, "available"] = "no"
        data.to_csv("hotels.csv", index=False)

    def available(self):
      
        availability = data.loc[data["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_data in data_cards:
            return True
        else:
            return False


class SecureCreditCard(CreditCard):   #inheritance
    def authenticate(self, given_password):
        password = data_cards_security.loc[data_cards_security["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False
        
class SpaReservation():
    def book_spa(self):
        pass



print(data)
hotel_ID = input("Enter the id of the hotel: ")
hotel = Hotel(hotel_ID)

if hotel.available():
    credit_card = SecureCreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26", holder="JOHN SMITH", cvc="123"):
        if credit_card.authenticate(given_password="mypass"):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            print(reservation_ticket.generate())
        else:
            print("Credit card authentication failed.")
    else:
        print("There was a problem with your payment")
    spa_request = input('Do you want a Spa Reservation:')
    if spa_request == 'yes':
        print('Thank you for booking your spa session')
    else:
        print('Enjoy your stay here!')
else:
    print("Hotel is not free.")
