from datetime import datetime
from math import ceil
import json
import os
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

        json_exists = self.does_cpm_json_exist()
        if json_exists:
            self.load_instances_from_json()

    # This function can be used when checking in a car,
    # This function returns a True or False based on if the parking garage is full or not
    def check_in(self, license_plate: str, checkin_datetime=datetime.now()) -> bool:
        if not self.is_car_parked_already(license_plate):
            # First we if the parking garage isn't at max capacity
            if len(self.parked_cars) < self.capacity:
                # Insert the cars basic information into the JSON file
                if self.json_insert_parkedcar(license_plate, checkin_datetime):
                    # Then we create a ParkedCar instance with the license plate and datetime.now()
                    car = ParkedCar(license_plate, checkin_datetime)
                    # We then add the ParkedCar instance to our ParkedCars dict with our license plate as its Key
                    self.parked_cars.update({license_plate: car})
                    # Log a new line
                    self.machinelogger.log_newline(license_plate, "check-in")
                    # If the car could be "Parked" "successfully" return a True
                    return True
                # Return a false if an error occurs when we try to save our parked car to the JSON file
                else:
                    return False
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
        # Log a new line
        self.machinelogger.log_newline(license_plate, "check-out", parking_fee)
        # Remove the car from our dict
        self.parked_cars.pop(license_plate)
        # Remove the car from our cpm's JSON file
        self.json_delete_parkedcar(license_plate)
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
    # running for the json file associated with this cpm
    def does_cpm_json_exist(self):
        # Put a try-except around it to handle a FileNotFoundError if the file isn't in the folder
        try:
            file = open(f'{self.machine_id}.json')
            file.close()
            return True
        except FileNotFoundError:
            return False

    # This function loads the parkedcar instances from the JSON file
    # whenever the cpm restarts and detects it has an associated JSON file
    def load_instances_from_json(self):
        # Open the file (in READ-ONLY mode)
        file = open(f'{self.machine_id}.json', 'r')
        # load the JSON data from the file
        json_data = json.load(file)
        # close the file
        file.close()

        # Iterate through the rows of the JSON data
        for row in json_data:
            # Create an instance of the ParkedCar class with the required data
            parked_car = ParkedCar(row['license_plate'], datetime.strptime(row["check_in"], "%m-%d-%Y %H:%M:%S"))
            # Add the instance to the parked_cars variable of our cpm
            self.parked_cars[row['license_plate']] = parked_car

    # This function checks if the car isn't already parked in another garage
    def is_car_parked_already(self, license_plate: str) -> bool:
        # Declare the return value and set it as False by default
        return_value = False
        # Loop through the files in the directory in which this script is run
        for file in os.listdir():
            # If we find a file that ends with ".json" and isn't a file for this cpm then we open the file
            # and see if the car is already parked in another garage
            if file.endswith(".json") and file != f"{self.machine_id}.json":
                # Open the file
                file = open(file, 'r')
                # Load the JSON data
                json_data = json.load(file)
                # Close the file
                file.close()

                # Iterate through the cars in the file
                for car in json_data:
                    # If the license plate is the same as the car we are currently
                    # checking for, then set the return value to True
                    if license_plate == car['license_plate']:
                        return_value = True

        # Return the result
        return return_value

    # This function inserts a parkedcar into the cpm's associated JSON file
    def json_insert_parkedcar(self, license_plate: str, checkin_datetime: datetime):
        # Put a try-except around it the handle the errors
        try:
            # Check to see if a JSON file already exists
            # If it does, We can safely load its data to add up on.
            # If not, Then we don't load any data and just insert our car in a new JSON file
            if self.does_cpm_json_exist():
                # Open the file in READ/WRITE mode
                file = open(f'{self.machine_id}.json', 'r+')
                # Load the JSON data
                json_data = json.load(file)
            else:
                # Create the file in WRITE mode
                file = open(f'{self.machine_id}.json', 'w')
                # write into the file two brackets to make it a valid JSON
                file.write("[]")
                # Close the file
                file.close()
                # Reopen the file in READ/WRITE mode
                file = open(f'{self.machine_id}.json', 'r+')
                # Load the file as JSON data
                json_data = json.load(file)

            # Append to the JSON data our new parked car instance
            json_data.append({"license_plate": license_plate,
                              "check_in": checkin_datetime.strftime("%m-%d-%Y %H:%M:%S")})
            # Seek position 0
            file.seek(0)
            # Dump the json_data into the JSON file (with an indent of 4)
            json.dump(json_data, file, indent=4)
            # Close the file
            file.close()

            # Return a True on success
            return True
        except FileNotFoundError:
            return False

    # This function deletes a parkedcar from our cpm's associated JSON file
    def json_delete_parkedcar(self, license_plate: str):
        # Put a try-except around it the handle the errors
        try:
            # First, we retrieve all the data from the JSON file
            # Open the file
            file = open(f"{self.machine_id}.json", "r")
            # Load the JSON data
            json_data = json.load(file)
            # Close the file
            file.close()

            # Second, we remove the instance of our parked car from the data
            # Create a list in which we will store our new json data without the parked car instance
            new_json_data = list()
            # Iterate through the current json_data
            for car in json_data:
                # If we detect, the current car's license plate is different from the car we want to remove.
                # Then we add that car data to our new_json_data list
                if license_plate != car['license_plate']:
                    new_json_data.append(car)

            # Third, We write our new data to the file
            # Open the file in WRITE mode
            file = open(f"{self.machine_id}.json", "w")
            # Seek position 0
            file.seek(0)
            # JSON dump the information into the file with a indent of 4
            json.dump(new_json_data, file, indent=4)
            # Close the file
            file.close()

            # Return a True on succesfull completion
            return True
        except FileNotFoundError:
            return False


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
