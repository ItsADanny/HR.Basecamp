from datetime import datetime


class ParkedCar:
    def __init__(self, license_plate: str, check_in: datetime):
        self.license_plate = license_plate
        self.check_in = check_in


class CarParkingMachine:
    # DEFAULT VALUES FOR THE CarParkingMachine CLASS
    capacity = 10
    hourly_rate = 2.5
    parked_cars = {}

    # This function will run when the class is initiated
    def __init__(self, capacity, hourly_rate):
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = {}

    def get_parking_fee(self, license_plate: str):
        car = self.parked_cars.get(license_plate)
        check_in = datetime.strptime(car.check_in, "%Y-%m-%d %H:%M:%S")
        end_time = datetime.strptime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        hour_time_difference = (end_time - check_in) * 3600
        if hour_time_difference >= round(hour_time_difference, 0):
            hour_time_difference = round(hour_time_difference, 0) + 1
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
