from datetime import date
from enum import Enum

#Used ENUM since there are 2 options for paying
class PaymentMethod(Enum):
    CREDIT_CARD = "Credit Card"
    CASH = "Cash"

# A  class for room with it attributes
class Room:
    def __init__(self, room_number: int, room_type: str, price_per_night: int, availability_status: bool):
        self.__room_number = room_number
        self.__type = room_type
        self.__price_per_night = price_per_night
        self.__availability_status = availability_status
#return room details in a dictionary formate
    def get_room_details(self):
        return {
            "Room Number": self.__room_number,
            "Type": self.__type,
            "Price Per Night": self.__price_per_night,
            "Available": self.__availability_status
        }
#To check if the room is available or not
    def check_availability(self):
        return self.__availability_status
#Updates the room availability
    def update_availability(self, status: bool):
        self.__availability_status = status

# A  class for guest with it attributes
class Guest:
    def __init__(self, guest_id: int, name: str, contact_info: str):
        self.__guest_id = guest_id
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_points = 0
#register the guest
    def register_guest(self, name, contact):
        self.__name = name
        self.__contact_info = contact

#update the guest profile
    def update_profile(self, contact):
        self.__contact_info = contact

    def view_reservation_history(self):
        pass

    def get_guest_id(self):
        return self.__guest_id

    def get_name(self):
        return self.__name

# A  class for loyalty program with it attributes
class LoyaltyProgram:
    def __init__(self, loyalty_id: int, guest: Guest, points: int = 0):
        self.__loyalty_id = loyalty_id
        self.__guest = guest
        self.__points = points

    def earn_points(self, amount: int):
        self.__points += amount

    def redeem_rewards(self):
        pass

    def view_points(self):
        return self.__points

# A  class for booking with it attributes
class Booking:
    def __init__(self, booking_id: int, guest: Guest, room: Room, check_in_date: date, check_out_date: date,
                 total_price: int, status: str):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__total_price = total_price
        self.__status = status
        self.__invoice = Invoice(booking_id, self, total_price, PaymentMethod.CREDIT_CARD, date.today()) #to create invoice

    def create_booking(self):
        pass

    def cancel_booking(self):
        pass

    def get_booking_details(self):
        return {
            "Booking ID": self.__booking_id,
            "Guest": self.__guest.get_name(),
            "Room": self.__room.get_room_details(),
            "Check-in": self.__check_in_date,
            "Check-out": self.__check_out_date,
            "Total Price": self.__total_price,
            "Status": self.__status
        }

# A  class for invoice with it attributes
class Invoice:
    def __init__(self, invoice_id: int, booking: Booking, amount: int, payment_method: PaymentMethod,
                 date_issued: date):
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method
        self.__date_issued = date_issued

# generate invoice details  as a dictionary
    def generate_invoice(self):
        return {
            "Invoice ID": self.__invoice_id,
            "Booking ID": self.__booking.get_booking_details()["Booking ID"],
            "Amount": self.__amount,
            "Payment Method": self.__payment_method.value,
            "Date Issued": self.__date_issued
        }

    def view_invoice(self):
        return self.generate_invoice()

# A  class for service request with it attributes
class ServiceRequest:
    def __init__(self, request_id: int, guest: Guest, service_type: str, status: str):
        self.__request_id = request_id
        self.__guest = guest
        self.__service_type = service_type
        self.__status = status

    def create_request(self, guest, service):
        pass

    def update_status(self, status):
        self.__status = status

    def view_request_details(self):
        return {
            "Request ID": self.__request_id,
            "Guest": self.__guest.get_name(),
            "Service Type": self.__service_type,
            "Status": self.__status
        }
#Test Case1
guest = Guest(101, "Mahra Abdulkarim", "mahra123@mail.com")
room = Room(303, "Single", 500, True)
booking = Booking(1001, guest, room, date(2025, 3, 30), date(2025, 4, 2), 300, "Confirmed")

# Generate invoice from the booking
invoice = booking._Booking__invoice  # Accessing the private invoice attribute for testing purpose
print(invoice.generate_invoice())  # This will output the invoice details

#Test Case2
guest = Guest(102, "Nouf Abdulkarim", "Nouf285@email.com")
service_request = ServiceRequest(201, guest, "Room Service", "Pending")
# Update the status of the service request
service_request.update_status("Completed")
# View the updated service request details
print(service_request.view_request_details())  # This will output the updated service request details


print("\n**********PART C ************")

from datetime import date

#Classes
class Guest:
    def __init__(self, guest_id, name, contact_info, loyalty_status="Regular"):
        self.guest_id = guest_id
        self.name = name
        self.contact_info = contact_info
        self.loyalty_status = loyalty_status
        self.history = []

    def __str__(self):
        return f"Guest {self.name} ({self.loyalty_status})"

    def add_reservation(self, booking):
        self.history.append(booking)

    def view_history(self):
        print(f"{self.name}'s Reservation History:")
        for b in self.history:
            print(b)

class Room:
    def __init__(self, room_number, room_type, price_per_night, availability_status=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.availability_status = availability_status

    def __str__(self):
        return f"Room {self.room_number} ({self.room_type})"

    def check_availability(self):
        return self.availability_status

    def update_status(self, status):
        self.availability_status = status

class Booking:
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date):
        self.booking_id = booking_id
        self.guest = guest
        self.room = room
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        self.status = "Pending"

    def make_reservation(self):
        if not self.room.check_availability():
            print("Room not available!")
            return False
        self.room.update_status(False)
        self.status = "Confirmed"
        self.guest.add_reservation(self)
        print(f"Reservation confirmed for {self.guest.name} in Room {self.room.room_number}")
        return True

    def cancel_reservation(self):
        self.status = "Cancelled"
        self.room.update_status(True)
        print(f"Reservation {self.booking_id} cancelled")
        return True

    def __str__(self):
        return f"Booking {self.booking_id} for {self.guest.name} in Room {self.room.room_number} ({self.status})"

class Invoice:
    def __init__(self, invoice_id, booking, additional_charges=0.0, discounts=0.0):
        self.invoice_id = invoice_id
        self.booking = booking
        self.additional_charges = additional_charges
        self.discounts = discounts
        self.total_amount = self.calculate_total()
        self.payment = None

    def calculate_total(self):
        nights = (self.booking.check_out_date - self.booking.check_in_date).days
        return (self.booking.room.price_per_night * nights) + self.additional_charges - self.discounts

    def set_payment(self,payment_method):
        self.payment = payment_method

    def generate_invoice(self):
        details = {
            "Invoice ID": self.invoice_id,
            "Booking ID": self.booking.booking_id,
            "Guest": self.booking.guest.name,
            "Room": self.booking.room.room_number,
            "Check-in": self.booking.check_in_date,
            "Check-out": self.booking.check_out_date,
            "Total": f"${self.total_amount:.2f}",
            "Payment Method": self.payment if self.payment else "Pending"
        }
        for k, v in details.items():
            print(f"{k}: {v}")

# Test Cases
print("\n--- Guest Account Creation ---")
g1 = Guest(1, "Mahra", "Mahra123@mail.com")
g2 = Guest(2, "Nouf", "Nouf285@mail.com", "Gold")
print(g1)
print(g2)

print("\n--- Searching for Available Rooms ---")
r1 = Room(101, "Single", 500)
r2 = Room(102, "Suite", 700)
print(r1.check_availability())
print(r2.check_availability())

print("\n--- Making a Room Reservation ---")
b1 = Booking(1, g1, r1, date(2025, 4, 1), date(2025, 4, 4))
b2 = Booking(2, g2, r2, date(2025, 5, 1), date(2025, 5, 3))
b1.make_reservation()
b2.make_reservation()

print("\n--- Invoice Generation ---")
i1 = Invoice(1, b1, additional_charges=50, discounts=25)
i1.generate_invoice()


print("\n--- Booking Confirmation  ---")
print(b1.status)
print(b2.status)

print("\n--- Payment Processing ---")
# Create invoices for the bookings with different payment methods
i1 = Invoice(1, b1, additional_charges=50, discounts=25)
i2 = Invoice(2, b2, additional_charges=100, discounts=70)
# Set different payment methods
i1.set_payment("CreditCard")
i2.set_payment("MobileWallet")

# Generate invoices to verify the payments and totals
i1.generate_invoice()
i2.generate_invoice()

print("\n--- Reservation History ---")
g1.view_history()
g2.view_history()

print("\n--- Cancellation ---")
b1.cancel_reservation()
b2.cancel_reservation()


