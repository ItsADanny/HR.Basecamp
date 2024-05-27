from datetime import datetime
from math import ceil
# ParkedCar class to store information of parked cars.


# Here we declare our ParkedCar class
class ParkedCar:
    # When we initiate the class, this will be set as the classes information
    def __init__(self, license_plate: str, check_in: datetime):
        # Here we assign the license plate, so we can see what the license plate is for the parked car
        self.license_plate = license_plate
        # Here we assign the datetime for when the car is parked, This will later be used to calculate
        # the required amount of parking fee that has to be paid by the owner of the car
        self.check_in = check_in


class CarParkingMachine:
    # When we initiate the class, this will be set as the classes information
    def __init__(self, id, capacity=10, hourly_rate=2.5, parked_cars=None):
        if parked_cars is None:
            parked_cars = dict()
        self.machine_id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars
        self.machinelogger = CarParkingLogger(id)

    # This function can be used when checking in a car,
    # This function returns a True or False based on if the parking garage is full or not
    def check_in(self, license_plate: str, checkin_datetime=datetime.now()) -> bool:
        # First we if the parking garage isn't at max capacity
        if len(self.parked_cars) < self.capacity:
            # Then we create a ParkedCar instance with the license plate and datetime.now()
            car = ParkedCar(license_plate, checkin_datetime)
            # We then add the ParkedCar instance to our ParkedCars dict with our license plate as its Key
            self.parked_cars.update({license_plate: car})
            # Log a new line
            self.machinelogger.log_newline(license_plate, "check-in")
            # If the car could be "Parked" "successfully" return a True
            return True
        # Return a False if the parking garage is full
        return False

    # This function can be used when checking out a car,
    # This function returns a float that contains the Parking fee that needs to be paid
    def check_out(self, license_plate: str) -> float:
        # Use the get_parking_fee function of the CarParkingMachine class to get the parking fee
        parking_fee = self.get_parking_fee(license_plate)
        # Log a new line
        self.machinelogger.log_newline(license_plate, "check-out", parking_fee)
        # Remove the car from our dict
        self.parked_cars.pop(license_plate)
        # Return the parking fee
        return parking_fee

    # This function can be used to get the parking fee for a certain car based on its license plate,
    # This function returns a float which contains the Parking fee for the car based on its license plate
    def get_parking_fee(self, license_plate: str):
        # First, we retrieve the car from our dictionary
        car = self.parked_cars.get(license_plate)
        # Second, we retrieve the cars checkin datetime
        car_starttime = car.check_in
        # Third, we calculate the time the car has been parked
        parking_time = ceil((datetime.now() - car_starttime).total_seconds() / 3600)
        # Calculate the parking fee
        parking_fee = round(min(parking_time, 24) * self.hourly_rate, 2)
        # Return the results
        return parking_fee


class CarParkingLogger:

    def __init__(self, machine_id):
        self.machine_id = machine_id

    # This function gets the total fees for a certain machine based on the given machine identifier and search date
    def get_machine_fee_by_day(self, machine_id: str, search_date: str) -> float:
        if search_date[2] == '-' and search_date[5] == '-' and len(search_date) == 10:
            # Create a float in which we will store our total parking fee
            fee_total = 0.0

            # Open the file in READ-ONLY mode
            logfile = open("carparklog.txt", "r")
            for logline in logfile:
                splitted_logline = logline.split(";")
                # Retrieve the datetime part
                logline_datetime = splitted_logline[0]
                # Check if the selected machine and the machine in the line are the same
                # and check if the action is "check-out"
                if (splitted_logline[1].replace("cpm_name=", "") == machine_id
                        and splitted_logline[3].replace("action=", "") == "check-out"):
                    if logline_datetime[0:10] == search_date:
                        fee_total += int(splitted_logline[4].replace("parking_fee=", ""))

            # Return the result
            return fee_total
        else:
            # Return -1.0 if the date is invalid
            return -1.0

    def get_total_car_fee(self, license_plate: str) -> float:
        # Create a float in which we will store our total parking fee
        fee_total = 0.0

        # Open the file in READ-ONLY mode
        logfile = open("carparklog.txt", "r")
        for logline in logfile:
            splitted_logline = logline.split(";")
            # Check if the action is "check-out"
            if splitted_logline[3].replace("action=", "") == "check-out":
                logline_parkingfee = int(splitted_logline[4].replace("parking_fee=", ""))
                if license_plate == splitted_logline[2].replace("license_plate=", ""):
                    fee_total += logline_parkingfee

        # Return the result
        return fee_total

    def log_newline(self, license_plate: str, action: str, parking_fee=0.0) -> bool:
        # Create an empty string in which we will store our logline
        logline = ""

        # Open the log file in APPEND MODE
        logfile = open("carparklog.txt", "a")

        # CODEGRADE PROBLEM
        # Declare a variable in which we store our current datetime string
        log_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        # Check if the action preformed is a "check-in" else use a "check-out" line
        if action == "check-in":
            logline = (f"{log_datetime};cpm_name={self.machine_id};"
                       f"license_plate={license_plate};action={action}\n")
        else:
            logline = (f"{log_datetime};cpm_name={self.machine_id};"
                       f"license_plate={license_plate};action={action};parking_fee={parking_fee}\n")

        # Write the log to the file
        logfile.write(logline)
        # Close the file
        logfile.close()


def main():
    parking_machine = CarParkingMachine("1")

    input_user = ""
    while input_user.lower() != "q":
        print("[I] Check-in car by license plate")
        print("[O] Check-out car by license plate")
        print("[Q] Quit program")
        input_user = input("Option: ").lower()

        if input_user == "i":
            input_user_license_plate = input("Please enter your license plate number: ")
            if parking_machine.check_in(input_user_license_plate):
                print("license registered")
            else:
                print("Capacity reached")
        elif input_user == "o":
            input_user_license_plate = input("Please enter your license plate number: ")
            parking_fee_result = parking_machine.check_out(input_user_license_plate)
            if parking_fee_result:
                print(f"Parking fee: {parking_fee_result} euro")
            else:
                print("License plate not found, Please try again")
        elif input_user == "q":
            print("Goodbye!")
        else:
            print("Invalid input, Please try again")


if __name__ == "__main__":
    main()
