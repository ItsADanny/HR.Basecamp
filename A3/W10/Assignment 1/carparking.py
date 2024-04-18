# Here we import the only part required from the datetime module
from datetime import datetime


# Here we declare our ParkedCar class
class ParkedCar:
    # When we initiate the class this will be set as the classes information
    def __init__(self, license_plate: str, check_in: datetime):
        # Here we assign the license plate so we can see what the license plate is for the parked car
        self.license_plate = license_plate
        # Here we assign the datetime for when the car is parked, This will later be used to calculate
        # the required amount of parking fee that has to be paid by the owner of the car
        self.check_in = check_in


class CarParkingMachine:
    # DEFAULT VALUES FOR THE CarParkingMachine CLASS
    capacity = 10
    hourly_rate = 2.5
    parked_cars = {}

    # When we initiate the class this will be set as the classes information
    def __init__(self, id, capacity, hourly_rate):
        self.id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    # This function is used to get the fee for parking the car
    def get_parking_fee(self, license_plate: str):
        # First, we retrieve the car from our dictionary
        car = self.parked_cars.get(license_plate)
        # Second, We retrieve from our car's class item what the checkin time was
        check_in = car.check_in
        # Third, We get the current datetime
        end_time = datetime.now()
        # Fourth, We calculate the time between the 2 times in hours
        hour_time_difference = (end_time - check_in) * 3600
        # Fifth, We account for rounding up the hours
        if hour_time_difference >= round(hour_time_difference, 0):
            hour_time_difference = round(hour_time_difference, 0) + 1
        # Finally, we return the hourly rate for the parking machine times the hours the car was in the parking garage
        return self.hourly_rate * hour_time_difference

    def check_in(self, license_plate: str):
        if len(self.parked_cars) < 11:
            car = ParkedCar(license_plate, datetime.now())
            self.parked_cars.update({license_plate: car})
            return True
        return False

    def check_out(self, license_plate: str):
        parking_fee = self.get_parking_fee(license_plate)
        self.parked_cars.pop(license_plate)
        return parking_fee


def main():
    parking_machine = CarParkingMachine(10, 2.5)

    input_user = ""
    while input_user.lower() != "q":
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        input_user = input("Option: ").lower()

        if input_user == "i":
            input_user_license_plate = input("Please enter your license plate number: ")
            parking_machine.check_in(input_user_license_plate)
        elif input_user == "o":
            input_user_license_plate = input("Please enter your license plate number: ")
            parking_machine.check_out(input_user_license_plate)
        elif input_user == "q":
            print("Goodbye!")
        else:
            print("Invalid input, Please try again")


if __name__ == "__main__":
    main()
