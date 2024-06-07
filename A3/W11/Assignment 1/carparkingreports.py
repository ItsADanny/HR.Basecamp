# Import the required modules/functions/methods
from datetime import datetime

# DEBUGGING MENU
# ======================================================================================================================
# To show all debugging prints in this script, please set this debugging boolean to True
# If you want to see certain debugging field, you can enable them by changing the booleans
# ======================================================================================================================
# Show all debugging
# -------------------------------------------------------------------
show_debugging = False

# Debugging prints - Function: gen_report_allcars_date_machine
# -------------------------------------------------------------------
# Show all available debugging for this function
show_all_debugging_ac_dm = False
# Show File data from "carparkinglog.txt"
show_debugging_ac_dm_filedata = False
# Show File data per row from "carparkinglog.txt"
show_debugging_ac_dm_row_filedata = False
# Show lines in list_report_data
show_debugging_list_report_data = False

# Debugging prints - Function: gen_report_totalfees_date
# -------------------------------------------------------------------
# Show all available debugging for this function
show_all_debugging_tf_d = False
# Show File data from "carparkinglog.txt"
show_debugging_tf_d_filedata = False
# Show File data per row from "carparkinglog.txt"
show_debugging_tf_d_row_filedata = False
# Show Datetime variables
show_debugging_tf_d_datetime_vars = False
# Show items in dict_fee_total_per_cpm dict
show_debugging_tf_d_dict = False
# Show lines in list_fee_total_per_cpm
show_debugging_tf_d_list = False

# ======================================================================================================================


# This function will generate a csv file that contains all parked cars for a
# specific machine based on the from and to date
def gen_report_allcars_date_machine(machine: str, from_date: str, to_date: str) -> [bool, str]:
    # Surround the function with a try-expect to handle any errors
    try:
        # Turn the from and to date strings into datetime objects
        datetime_from_date = datetime.strptime(from_date, '%d-%m-%Y')
        datetime_to_date = datetime.strptime(to_date, '%d-%m-%Y')

        # Create a list in which we will store the parking instances
        list_parking_instances = list()
        # Create a list in which we will store our data for the report
        list_report_data = list()

        # Open the carparklog.txt file
        file = open("carparklog.txt", "r")
        # Read the data from the file
        data = file.readlines()
        # Close the file
        file.close()

        # //Debugging - File data
        # ------------------------------------------------------------------
        if show_debugging or show_all_debugging_ac_dm or show_debugging_ac_dm_filedata:
            print(data)

        # Loop through the data row by row
        for row in data:
            # //Debugging - Row - File data
            # ------------------------------------------------------------------
            if show_debugging or show_all_debugging_ac_dm or show_debugging_ac_dm_row_filedata:
                print(row)

            # Turn the row into a list to access all the data
            list_row = row.split(';')
            # Turn the list into the required separate variables (And clean them up)
            datetime_log_dt = datetime.strptime(list_row[0], '%d-%m-%Y %H:%M:%S')
            string_log_cpm = list_row[1].replace("cpm_name=", "")
            string_log_lp = list_row[2].replace("license_plate=", "")
            string_log_action = list_row[3].replace("action=", "").replace("\n", "")

            # //Debugging - Datetime variables
            # ------------------------------------------------------------------
            if show_debugging or show_all_debugging_tf_d or show_debugging_tf_d_datetime_vars:
                print(f"DEBUGGING - datetime_log_dt    : {datetime_log_dt}")
                print(f"DEBUGGING - datetime_from_date : {datetime_from_date}")
                print(f"DEBUGGING - datetime_to_date   : {datetime_to_date}")

            # Check to see if the datetime of a log row is between the from and to date,
            # and check if it is for the selected cpm
            if datetime_from_date <= datetime_log_dt <= datetime_to_date and string_log_cpm == machine:
                # Create a variable to see if we already have an instance of this license plate
                instance_exists = False
                # Iterate through our instances to see if it already exists, if so then set instance_exists to True
                for instance in list_parking_instances:
                    if instance["license-plate"] == string_log_lp:
                        instance_exists = True

                if instance_exists:
                    for instance in list_parking_instances:
                        if instance["license-plate"] == string_log_lp:
                            # Check what the action of the log row is,
                            # and preform the need actions based on the action type
                            if string_log_action == "check-in":
                                # Update the instance with the check-in time
                                instance["checkin-datetime"] = datetime_log_dt
                            else:
                                # Retrieve the parking fee
                                float_log_parkingfee = float(list_row[4].replace("parking_fee=", ""))
                                # Update the instance with the check-out time and the parking fee
                                instance["checkout-datetime"] = datetime_log_dt
                                instance["parking-fee"] = float_log_parkingfee

                                # Here we preform a check to see if the instance is now fully complete
                                # If so, we save its data as a row for our report and clear the instance
                                # of any data for a next use of the license plate
                                if (instance["checkin-datetime"] != "" and instance["checkout-datetime"] != ""
                                        and instance["parking-fee"] != 0.0):
                                    # Create a new string which holds the data for our instance
                                    str_new_report_row = (f"{instance["license-plate"]};{instance["checkin-datetime"]};"
                                                          f"{instance["checkout-datetime"]};"
                                                          f"{instance["parking-fee"]}\n")
                                    # Append the data to our list that holds the report data
                                    list_report_data.append(str_new_report_row)
                                    # Clear nearly all the data from the instance except for the license plate
                                    instance["checkin-datetime"] = ""
                                    instance["checkout-datetime"] = ""
                                    instance["parking-fee"] = 0.0
                else:
                    # Create a new instance dict and pre-declare the license-plate
                    dict_new_instance = {"license-plate": string_log_lp, "checkin-datetime": "",
                                         "checkout-datetime": "", "parking-fee": 0.0}

                    # Check what the action of the log row is, and preform the need actions based on the action type
                    if string_log_action == "check-in":
                        # Update our new instance with the check-in datetime
                        dict_new_instance["checkin-datetime"] = datetime_log_dt
                    else:
                        # Retrieve the parking fee
                        float_log_parkingfee = float(list_row[4].replace("parking_fee=", ""))
                        # Update our new instance with the check-out datetime and parking fee
                        dict_new_instance["checkout-datetime"] = datetime_log_dt
                        dict_new_instance["parking-fee"] = float_log_parkingfee

                    # Append the new instance to our list with the other instances
                    list_parking_instances.append(dict_new_instance)

        # //Debugging - print list list_report_data
        # ------------------------------------------------------------------
        if show_debugging or show_all_debugging_tf_d or show_debugging_list_report_data:
            print(list_report_data)

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

    # When an error occurs, we will send back a False and the error that has occurred
    except Exception as e:
        return [False, str(e)]


# This function will generate a csv file that contains the total parking fees
# per machine based on a specific from and to date
def gen_report_totalfees_date(from_date: str, to_date: str) -> [bool, str]:
    # Surround the function with a try-expect to handle any errors
    try:
        # Turn the from and to date strings into datetime objects
        datetime_from_date = datetime.strptime(from_date, '%d-%m-%Y')
        datetime_to_date = datetime.strptime(to_date, '%d-%m-%Y')

        # Create an empty dict that will be used to store the total fee per machine
        dict_fee_total_per_cpm = dict()
        # Create a list in which we will store the completed results that will be writen to the csv report
        list_fee_total_per_cpm = list()

        # Open the carparklog.txt file
        file = open("carparklog.txt", "r")
        # Read the data from the file
        data = file.readlines()
        # Close the file
        file.close()

        # //Debugging - File data
        # ------------------------------------------------------------------
        if show_debugging or show_all_debugging_tf_d or show_debugging_tf_d_filedata:
            print(data)

        # Loop through the data row by row
        for row in data:
            # //Debugging - Row - File data
            # ------------------------------------------------------------------
            if show_debugging or show_all_debugging_tf_d or show_debugging_tf_d_row_filedata:
                print(row)

            # Turn the row into a list to access all the data
            list_row = row.split(';')
            # Turn the list into the required separate variables (And clean them up)
            datetime_log_dt = datetime.strptime(list_row[0], '%d-%m-%Y %H:%M:%S')
            string_log_cpm = list_row[1].replace("cpm_name=", "")
            string_log_action = list_row[3].replace("action=", "")

            # //Debugging - Datetime variables
            # ------------------------------------------------------------------
            if show_debugging or show_all_debugging_tf_d or show_debugging_tf_d_datetime_vars:
                print(f"DEBUGGING - datetime_log_dt    : {datetime_log_dt}")
                print(f"DEBUGGING - datetime_from_date : {datetime_from_date}")
                print(f"DEBUGGING - datetime_to_date   : {datetime_to_date}")

            # Check to see if the datetime of a log row is between the from and to date
            if datetime_from_date <= datetime_log_dt <= datetime_to_date:
                # See what the action of the log is to determine to see if there is a parking fee
                # If so, then retrieve the parking fee and add it to the total parking fee for that cpm
                if string_log_action == "check-out":
                    # Retrieve the parking fee, clean it up and convert it into a float
                    float_log_parkingfee = float(list_row[4].replace("parking_fee=", ""))

                    # See if the cpm is already in the dict_fee_total_per_cpm dict,
                    # If not, then add the cpm to the dict_fee_total_per_cpm dict and
                    # set the current parking as its starting amount
                    # If it is, Then add the parking to the total
                    if string_log_cpm not in dict_fee_total_per_cpm:
                        dict_fee_total_per_cpm[string_log_cpm] = float_log_parkingfee
                    else:
                        dict_fee_total_per_cpm[string_log_cpm] += float_log_parkingfee

        # Iterate through the dict
        for item in dict_fee_total_per_cpm.items():
            # //Debugging - items in dict_fee_total_per_cpm dict
            # ------------------------------------------------------------------
            if show_debugging or show_all_debugging_tf_d or show_debugging_tf_d_dict:
                print(item)

            # Add the data from this to a string which will be appended to the data for the new csv file
            list_fee_total_per_cpm.append(f"{item[0]};{item[1]}\n")

        # //Debugging - print list list_fee_total_per_cpm
        # ------------------------------------------------------------------
        if show_debugging or show_all_debugging_tf_d or show_debugging_tf_d_list:
            print(list_fee_total_per_cpm)

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

    # When an error occurs, we will send back a False and the error that has occurred
    except Exception as e:
        return [False, str(e)]


# This function will display all the menu options
def print_menu():
    print("[P] Report all parked cars during a parking period for a specific parking machine")
    print("[F] Report total collected parking fee during a parking period for all parking machines")
    print("[Q] Quit program")


# This function will display an error message in a pretty way
def print_error_report(error: str):
    print("Error:")
    print("==================================================================")
    print(error)
    print("==================================================================")


# This is the main function for this script
def main():
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
