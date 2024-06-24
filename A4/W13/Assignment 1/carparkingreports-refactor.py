# Import the required modules
import sqlite3
import os
import sys
from datetime import datetime

# Database filename
sqlite_database_filename = "carparkingmachine.db"


def sql_tablecheck():
    # Make a connection to the database
    db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
    # Prepare a Query to make the parkings table if it doesn't exist
    query = '''CREATE TABLE IF NOT EXISTS parkings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    car_parking_machine TEXT NOT NULL,
    license_plate TEXT NOT NULL,
    check_in TEXT NOT NULL,
    check_out TEXT DEFAULT NULL,
    parking_fee NUMERIC DEFAULT 0 
    );'''
    # Execute a command to make sure that the parkings table does exist
    db_connection.execute(query)


def sql_get_allparking(machine: str) -> list:
    # Create an emtpy list
    return_list = list()

    # Connect to the database
    db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
    # Prepare the query
    query = "SELECT check_in, check_out, car_parking_machine, parking_fee FROM parkings WHERE car_parking_machine = ? AND parking_fee != 0"
    # Execute the query and retrieve the results
    results = db_connection.execute(query, [machine])
    # Iterate through the results
    for row in results:
        # Add a list per row to the list containing the results
        return_list.append([row[0], row[1], row[2]])

    # Return the results
    return return_list


def sql_get_parkingmachine_fees() -> list:
    # Create an emtpy list
    return_list = list()

    # Connect to the database
    db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
    # Prepare the query
    query = "SELECT check_in, car_parking_machine, parking_fee FROM parkings WHERE parking_fee != 0"
    # Execute the query and retrieve the results
    results = db_connection.execute(query)
    # Iterate through the results
    for row in results:
        # Add a list per row to the list containing the results
        return_list.append([row[0], row[1], row[2]])

    # Return the results
    return return_list


def sql_get_parkingactivities(license_plate: str) -> list:
    # Create an emtpy list
    return_list = list()

    # Connect to the database
    db_connection = sqlite3.connect(os.path.join(sys.path[0], sqlite_database_filename))
    # Prepare the query
    query = ("SELECT car_parking_machine, check_in, check_out, parking_fee FROM "
             "parkings WHERE license_plate = ? AND parking_fee != 0")
    # Execute the query and retrieve the results
    results = db_connection.execute(query, [license_plate])
    # Iterate through the results
    for row in results:
        # Add a list per row to the list containing the results
        return_list.append([row[0], row[1], row[2], row[3]])

    # Return the results
    return return_list


def gen_report_allcars_date_machine(machine: str, from_date: str, to_date: str) -> [bool, str]:
    # Get all the parking data for this machine from our SQLite database
    data = sql_get_allparking(machine)

    # Iterate through the data and filter out the data that is not between the two given dates
    for row in data:
        check_in, car_parking_machine, parking_fee
        row_checkin = row[0]
        row_carparking_machine = row[1]
        row_parkingfee = row[2]

    # Create a unique filename that will be used when we generate our report
    report_name = f"{datetime.now().strftime("%d%m%Y%H%M%S")}-carparkingactivities.csv"

    # Create the file and open it in WRITE MODE
    file = open(report_name, "w")
    # Write the csv headers to the file
    file.write("license_plate;check-in;check-out;parking_fee\n")
    # Write the data to the csv file
    file.writelines(list_report_data)
    # Close the file
    file.close()

    # Return the results
    return [True, report_name]


def gen_report_totalfees_date(from_date: str, to_date: str) -> [bool, str]:
    # Turn the two input variables into datetime objects
    datetime_from_date = datetime.strptime(from_date, '%d-%m-%Y')
    datetime_to_date = datetime.strptime(to_date, '%d-%m-%Y')

    # Create an empty dict that will store all the selected fees per cpm
    dict_cpm_fee_totals = dict()
    # Create an empty list which will store the data for the report
    list_fee_total_per_cpm = list()

    # Get a list with all the fees
    list_fees = sql_get_parkingmachine_fees()

    # Iterate through the list
    for fee in list_fees:
        # Check if the date is between the two selected dates
        if datetime_from_date <= datetime.strptime(fee[0], '%d-%m-%Y') <= datetime_to_date:
            # If so, check if the cpm is already available in our dict.
            # If so, Update the value in our dict
            # If not, Create the cpm in our dict
            if fee[1] not in dict_cpm_fee_totals:
                dict_cpm_fee_totals[fee[1]] = fee[2]
            else:
                dict_cpm_fee_totals[fee[1]] += fee[2]

    # Iterate through our dict with the totals
    for cpm in dict_cpm_fee_totals.items():
        # Append the cpm totals to our data for the file
        list_fee_total_per_cpm.append(f"{cpm[0]};{cpm[1]}\n")

    # Create a unique filename that will be used when we generate our report
    report_name = f"{datetime.now().strftime("%d%m%Y%H%M%S")}-totalcpmfees.csv"

    # Create the file and open it in WRITE MODE
    file = open(report_name, "w")
    # Write the csv headers to the file
    file.write("car_parking_machine;total_parking_fee\n")
    # Write the data to the csv file
    file.writelines(list_fee_total_per_cpm)
    # Close the file
    file.close()

    # Return the result and the filename
    return [True, report_name]


def gen_report_totalparkingactivi_lp(license_plate: str) -> [bool, str]:
    # Create an empty list which will store the data for the report
    list_parking_activities = list()

    # Get the data of the parking activities of the selected license plate
    pa_db_data = sql_get_parkingactivities(license_plate)

    # Iterate through the data and add it to the list_parking_activities
    for row in pa_db_data:
        list_parking_activities.append(f"{row[1]};{row[3]};{row[4]};{row[5]}")

    # Create a unique filename that will be used when we generate our report
    report_name = f"{datetime.now().strftime("%d%m%Y%H%M%S")}-totalcpmfees.csv"

    # Create the file and open it in WRITE MODE
    file = open(report_name, "w")
    # Write the csv headers to the file
    file.write("car_parking_machine;total_parking_fee\n")
    # Write the data to the csv file
    file.writelines(list_parking_activities)
    # Close the file
    file.close()

    # Return the result and the filename
    return [True, report_name]


# This function will display all the menu options
def print_menu():
    print("[P] Report all parked cars during a parking period for a specific parking machine")
    print("[F] Report total collected parking fee during a parking period for all parking machines")
    print("[C] Report all complete parkings over all parking machines for a specific car")
    print("[Q] Quit program")


# This function will display an error message in a pretty way
def print_error_report(error: str):
    print("Error:")
    print("==================================================================")
    print(error)
    print("==================================================================")


# This is the main function for this script
def main():
    # First, make sure that we have a database with the parkings table
    sql_tablecheck()
    # Then continue with the rest of the program
    # Stay in the loop until the user inputs the choice to exit the program
    while True:
        # Print the menu
        print_menu()
        # Request user input
        input_choice = input("Enter your choice: ").lower()
        # Determine the choice made by the user
        if input_choice == "p":
            # Request the required information
            input_machine_identifier = input("Parking machine identifier: ")
            input_from_date = input("From date: ")
            input_to_date = input("To date: ")
            # Generate a report for all parked cars during a certain period and for a certain machine
            gen_results = gen_report_allcars_date_machine(input_machine_identifier, input_from_date, input_to_date)
            if gen_results[0]:
                print(f"Report has been generated! The report can be found as: {gen_results[1]}")
            else:
                print("There was an error when generating the report.")
                print_error_report(gen_results[1])

        elif input_choice == "f":
            # Request the required information
            input_from_date = input("From date: ")
            input_to_date = input("To date: ")
            # Generate a report for the total
            gen_results = gen_report_totalfees_date(input_from_date, input_to_date)
            # If the report could be generated, print a success message,
            # if not, print an error with a separate message of which error has occurred
            if gen_results[0]:
                print(f"Report has been generated! The report can be found as: {gen_results[1]}")
            else:
                print("There was an error when generating the report.")
                print_error_report(gen_results[1])

        elif input_choice == "c":
            # Request the required information
            input_licenseplate = input("From date: ")
            # Generate a report for the total
            gen_results = gen_report_totalparkingactivi_lp(input_licenseplate)
            # If the report could be generated, print a success message,
            # if not, print an error with a separate message of which error has occurred
            if gen_results[0]:
                print(f"Report has been generated! The report can be found as: {gen_results[1]}")
            else:
                print("There was an error when generating the report.")
                print_error_report(gen_results[1])

        elif input_choice == "q":
            # Exit out of the program
            print("Exiting program, Goodbye!")
            break
        else:
            # When an invalid choice has been given, return an error message to the user
            print("Invalid choice, please input a valid choice")


# When the script is run as its own program, the main function will be called
if __name__ == "__main__":
    main()
