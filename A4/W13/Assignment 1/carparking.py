from datetime import datetime
from math import ceil
import json
import os
import sys
import sqlite3


sqlite_database_filename = 'carparkingmachine.db'


# Here we declare our ParkedCar class
class ParkedCar:
    # When we initiate the class, this will be set as the classes information
    def __init__(self, id: int, cpm: str, license_plate: str, check_in: datetime,
                 check_out: datetime, parking_fee: float):
        self.id = id
        self.cpm = cpm
        # Here we assign the license plate, so we can see what the license plate is for the parked car
        self.license_plate = license_plate
        # Here we assign the datetime for when the car is parked, This will later be used to calculate
        # the required amount of parking fee that has to be paid by the owner of the car
        self.check_in = check_in
        self.check_out = check_out
        self.parking_fee = parking_fee


class CarParkingMachine:
    # When we initiate the class, this will be set as the classes information
    def __init__(self, id, capacity=10, hourly_rate=2.5, parked_cars=None):
        if parked_cars is None:
            parked_cars = dict()
        self.machine_id = id
        self.capacity = capacity
        self.hourly_rate = hourly_rate
        self.parked_cars = parked_cars

        # Perform a check if the DB exists and if the table we need exists
        # If not, it will create both
        self.db_tablecheck()

        # Check if the file exists
        if self.does_db_file_exist():
            # Load the instances into the cpm
            self.load_instances()

    # This function will check if the required database table does exist
    def db_tablecheck(self):
        self.db_conn = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
        self.db_conn.execute(
            '''CREATE TABLE IF NOT EXISTS parkings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                car_parking_machine TEXT NOT NULL,
                license_plate TEXT NOT NULL,
                check_in TEXT NOT NULL,
                check_out TEXT DEFAULT NULL,
                parking_fee NUMERIC DEFAULT 0
            );'''
        )
        self.db_conn.close()

    # This function will return all active instances from the database that haven't checked-out yet
    def db_get_instances_for_machine(self):
        # Create an emtpy list
        return_list = list()

        # Connect to the database
        db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
        # Prepare the query
        query = "SELECT id, license_plate, check_in FROM parkings WHERE car_parking_machine = ? AND parking_fee = 0"
        # Execute the query and retrieve the results
        results = db_connection.execute(query, [self.machine_id])
        # Iterate through the results
        for row in results:
            # Add a list per row to the list containing the results
            return_list.append([row[0], row[1], row[2]])

        # Return the results
        return return_list

    # This function will return a car if it is already at another garage
    def db_get_instance_lp(self, license_plate: str):
        # Create an emtpy list
        return_list = list()

        # Connect to the database
        db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
        # Prepare the query
        query = "SELECT * FROM parkings WHERE license_plate = ? AND parking_fee != 0"
        # Execute the query and retrieve the results
        results = db_connection.execute(query, [license_plate])
        # Iterate through the results
        for row in results:
            # Add a list per row to the list containing the results
            return_list.append([row[0], row[1], row[2], row[3], row[4], row[5]])

        # Return the results
        return return_list

    # This function will retrieve the last checkin of the given license plate
    def db_get_list_insert_for_instance(self, license_plate: str) -> int:
        # Create an emtpy list
        instance_id = 0

        # Connect to the database
        db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
        # Prepare the query
        query = "SELECT id FROM parkings WHERE license_plate = ? AND parking_fee != 0"
        # Execute the query and retrieve the results
        results = db_connection.execute(query, [license_plate])
        # Iterate through the results
        for row in results:
            # Add a list per row to the list containing the results
            instance_id = row[0]

        # Return the results
        return instance_id

    # This function will insert a new car into the database
    def db_insert_instance(self, instance: ParkedCar) -> ParkedCar:
        db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
        query = "INSERT INTO parkings (car_parking_machine,license_plate,check_in) VALUES (?,?,?)"
        db_connection.execute(query,
                             [self.machine_id, instance.license_plate, instance.check_in.strftime("%m-%d-%Y %H:%M:%S")])
        db_connection.commit()
        db_connection.close()
        instance.id = self.db_get_list_insert_for_instance(instance.license_plate)
        return instance

    def db_update_car(self, instance: ParkedCar, check_out: datetime, parking_fee: float):
        db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
        query = ("UPDATE parkings SET car_parking_machine = ?, license_plate = ?, check_in = ?,"
                 " check_out = ?, parking_fee = ? WHERE id = ?")
        db_connection.execute(query,
                             [self.machine_id, instance.license_plate, instance.check_in.strftime("%m-%d-%Y %H:%M:%S"),
                              check_out.strftime("%m-%d-%Y %H:%M:%S"), parking_fee, instance.id])
        db_connection.commit()
        db_connection.close()

    # This function can be used when checking in a car,
    # This function returns a True or False based on if the parking garage is full or not
    def check_in(self, license_plate: str, checkin_datetime=datetime.now()) -> bool:
        if not self.is_car_parked_already(license_plate):
            # First we if the parking garage isn't at max capacity
            if len(self.parked_cars) < self.capacity:
                # Create an instance for the car
                parked_car = ParkedCar(1, self.machine_id, license_plate, checkin_datetime, datetime.now(), 0)
                # Insert the instance into the database and receive the instance back with its ID in the database
                parked_car = self.db_insert_instance(parked_car)
                # We then add the ParkedCar instance to our ParkedCars dict with our license plate as its Key
                self.parked_cars.update({license_plate: parked_car})

                # Log lines aren't necessary for this assignment
                # # Log a new line
                # self.machinelogger.log_newline(license_plate, "check-in")

                # If the car could be "Parked" "successfully" return a True
                return True
            # Return a False if the parking garage is full
            else:
                return False
        # Return a False if the car can't be parked because it is already parked in another garage
        else:
            return False

    # This function can be used when checking out a car,
    # This function returns a float that contains the Parking fee that needs to be paid
    def check_out(self, license_plate: str) -> float:
        # Use the get_parking_fee function of the CarParkingMachine class to get the parking fee
        parking_fee = self.get_parking_fee(license_plate)

        # Log lines aren't necessary for this assignment
        # # Log a new line
        # self.machinelogger.log_newline(license_plate, "check-out", parking_fee)

        # Update the car in our database
        self.db_update_car(self.parked_cars[license_plate], datetime.now(), parking_fee)

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

    # This function will search the folder in which the script is
    # running for the database file
    def does_db_file_exist(self):
        # Loop through the files in the current directory
        for file in os.listdir():
            # if we find the database file, we immediately return a True
            if file == sqlite_database_filename:
                return True
        # If we didn't find the file, we return a False
        return False

    # This function loads the parkedcar instances from the database
    def load_instances(self):
        # Get the data from the database
        data = self.db_get_instances_for_machine()

        for instance in data:
            self.parked_cars[instance[1]] = ParkedCar(instance[0], instance[1], self.machine_id,
                                                      datetime.strptime(instance[2], "%d-%m-%Y %H:%M:%S"),
                                                      datetime.now(), 0)

    # This function checks if the car isn't already parked in another garage
    def is_car_parked_already(self, license_plate: str) -> bool:
        # Declare the return value and set it as False by default
        return_value = False

        # Get the data from the database
        data = self.db_get_instance_lp(license_plate)

        if len(data) > 0:
            return_value = True

        return return_value


# class CarParkingLogger:
#
#     def __init__(self, machine_id):
#         self.machine_id = machine_id
#
#     # This function gets the total fees for a certain machine based on the given machine identifier and search date
#     def get_machine_fee_by_day(self, machine_id: str, search_date: str) -> float:
#         if search_date[2] == '-' and search_date[5] == '-' and len(search_date) == 10:
#             # Create a float in which we will store our total parking fee
#             fee_total = 0.0
#
#             # Open the file in READ-ONLY mode
#             logfile = open("carparklog.txt", "r")
#             for logline in logfile:
#                 splitted_logline = logline.split(";")
#                 # Retrieve the datetime part
#                 logline_datetime = splitted_logline[0]
#                 # Check if the selected machine and the machine in the line are the same
#                 # and check if the action is "check-out"
#                 if (splitted_logline[1].replace("cpm_name=", "") == machine_id
#                         and splitted_logline[3].replace("action=", "") == "check-out"):
#                     if logline_datetime[0:10] == search_date:
#                         fee_total += int(splitted_logline[4].replace("parking_fee=", ""))
#
#             # Return the result
#             return fee_total
#         else:
#             # Return -1.0 if the date is invalid
#             return -1.0
#
#     def get_total_car_fee(self, license_plate: str) -> float:
#         # Create a float in which we will store our total parking fee
#         fee_total = 0.0
#
#         # Open the file in READ-ONLY mode
#         logfile = open("carparklog.txt", "r")
#         for logline in logfile:
#             splitted_logline = logline.split(";")
#             # Check if the action is "check-out"
#             if splitted_logline[3].replace("action=", "") == "check-out":
#                 logline_parkingfee = int(splitted_logline[4].replace("parking_fee=", ""))
#                 if license_plate == splitted_logline[2].replace("license_plate=", ""):
#                     fee_total += logline_parkingfee
#
#         # Return the result
#         return fee_total
#
#     def log_newline(self, license_plate: str, action: str, parking_fee=0.0) -> bool:
#         # Create an empty string in which we will store our logline
#         logline = ""
#
#         # Open the log file in APPEND MODE
#         logfile = open("carparklog.txt", "a")
#
#         # CODEGRADE PROBLEM
#         # Declare a variable in which we store our current datetime string
#         log_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
#
#         # Check if the action preformed is a "check-in" else use a "check-out" line
#         if action == "check-in":
#             logline = (f"{log_datetime};cpm_name={self.machine_id};"
#                        f"license_plate={license_plate};action={action}\n")
#         else:
#             logline = (f"{log_datetime};cpm_name={self.machine_id};"
#                        f"license_plate={license_plate};action={action};parking_fee={parking_fee}\n")
#
#         # Write the log to the file
#         logfile.write(logline)
#         # Close the file
#         logfile.close()


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
                if len(parking_machine.parked_cars) >= 10:
                    print("Capacity reached")
                else:
                    print("An error has occured while trying to park the car")
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
