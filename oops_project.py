from abc import ABC, abstractmethod


class RideService:
    def __init__(self, name, rates):
        self.name = name
        self.rates = rates   

    def show_rates(self):
        print(f"--- {self.name} Ride Rates ---")
        for vehicle, rate in self.rates.items():
            print(f"{vehicle} : ₹{rate}/km")


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(Payment):
    def pay(self, amount):
        print(f"✅ Paid ₹{amount} via UPI")


class CardPayment(Payment):
    def pay(self, amount):
        print(f"✅ Paid ₹{amount} via Card")


class CashPayment(Payment):
    def pay(self, amount):
        print(f"💰 ₹{amount} to be paid in cash")



class User:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone



class Ride:
    def __init__(self, user, service):
        self.user = user
        self.service = service
        self.vehicle = None
        self.distance = 0

    def select_vehicle(self, vehicle):
        if vehicle in self.service.rates:
            self.vehicle = vehicle
            print(f"✅ {vehicle} selected")
        else:
            print("❌ Invalid vehicle")

    def set_distance(self, distance):
        self.distance = distance

    def calculate_fare(self):
        return self.service.rates[self.vehicle] * self.distance

    def show_summary(self):
        print("\n--- Ride Summary ---")
        print(f"User: {self.user.name}")
        print(f"Vehicle: {self.vehicle}")
        print(f"Distance: {self.distance} km")
        print(f"Total Fare: ₹{self.calculate_fare()}")


def main():
    print("🚗 Welcome to Ride Booking App")

    name = input("Enter your name: ")
    phone = input("Enter your phone: ")

    user = User(name, phone)

    rates = {
        "Bike": 10,
        "Car": 20,
        "Auto": 15
    }

    service = RideService("QuickRide", rates)
    service.show_rates()

    ride = Ride(user, service)

    vehicle = input("Choose vehicle: ").title()
    ride.select_vehicle(vehicle)

    distance = float(input("Enter distance (km): "))
    ride.set_distance(distance)

    ride.show_summary()

    print("\nChoose Payment Mode")
    print("1: Card")
    print("2: UPI")
    print("3: Cash")

    choice = input("Select: ")

    if choice == "1":
        payment = CardPayment()
    elif choice == "2":
        payment = UPIPayment()
    else:
        payment = CashPayment()

    payment.pay(ride.calculate_fare())


if __name__ == "__main__":
    main()
