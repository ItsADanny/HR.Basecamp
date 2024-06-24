# Here we import the required Python modules
import os
import json
import sqlite3

# In this variable we store the name for the database file
database_filename = "shipments.db"


# This is the main function of shipmentapp.py
# This function will be called when the script is run
def main():
    while True:
        # Print the menu items
        print_menu()
        # Request an input from the user
        input_choice_usr = input("Choice: ").lower()
        if input_choice_usr == "i":
            # Print some messages for the import function
            print("Please input the exact name of the file you want to import (Only .json is supported).")
            print("To exit this function, please input a [Q]")
            # Predefine the filename variable,
            # Once we have a valid filename we will then put
            # this filename into this variable
            filename = ""
            # Enter a loop until we receive a valid filename
            while True:
                # Request the filename from the user
                input_filename_usr = input("filename: ")
                # Check if the input from the user is the filename or q (to exit the program) else
                if input_filename_usr.endswith(".json"):
                    # Check if the file that has been inputted does exist
                    if file_checkexistence(input_filename_usr):
                        # If the filename ends with .json
                        # And if it does exist.
                        # Then set this as the filename and break out of the loop
                        filename = input_filename_usr
                        break
                    else:
                        print("File does not exist, Please input a valid file or exit this function with [Q]")
                elif input_filename_usr.lower() == "q":
                    # If the input is q then break out of the loop
                    break
                else:
                    # If the input is anything else, then print an error message
                    print("Invalid input, please input a valid filename or exit this function with [Q]")
            if filename != "":
                # Display a message that the import has started
                print("Import started")
                # Display the import result message
                print(import_data(input_filename_usr)[1])
        elif input_choice_usr == "q":
            # If the user selected Q then exit out of the program
            print("Exiting program")
            break
        else:
            # If the user inputted anything else then print an error message
            print("Invalid input, Please input a valid choice")


# This function prints the menu for the application
def print_menu():
    print("================================================")
    print("        Master Assignment - Shipment app")
    print("         A step into the world of cargo")
    print(" ")
    print("  Assignment by: Danny de Snoo, HR-nr: 1091749")
    print("================================================")
    print("[I] - Import data")
    print("[R] - Open reporter options")
    print("------------------------------------------------")
    print("[Q] - Exit program")
    print("================================================")


# This function will check if a certain file exists
def file_checkexistence(filename: str) -> bool:
    # Loop through the files in the current directory
    for file in os.listdir():
        # if we find the given file, we immediately return a True
        if file == filename:
            return True
    # If we didn't find the file, we return a False
    return False


# This function will import the data
def json_get_filedata(filename: str) -> [bool, str, dict]:
    # Check to see if the file exists
    if file_checkexistence:
        # Open the file
        file = open(filename, "r")
        # Load the data
        json_data = json.load(file)
        # Close the file
        file.close()
        # create the results with the JSON data
        return_result = [True, "JSON data loaded", json_data]
    else:
        # create the results with an empty dict and a "File not found" message
        return_result = [False, "File not found", dict()]

    # Send back the result
    return return_result


# This function will import the data from the json file
def import_data(filename: str) -> [bool, dict]:
    # Predefine the result we are going to send back
    return_result = [False, {"total_records": 0, "succesfull_inserts": 0, "unsuccesfull_inserts": 0, "errors": list()}]
    # Make a list that will temporarily store our internal_shipments_id's
    # This will be used to see if everything went successfully
    temp_list_internal_shipment_ids = list()
    # Load the JSON data
    json_data = json_get_filedata(filename)
    # Check if the JSON data load was succesfull
    if json_data[0]:
        # Update our return dict with the number of records we are processing
        return_result[1]["total_records"] = len(json_data[2])
        # Create a connection to the mysql database
        db_conn = sqlite3.connect(database_filename)
        # Iterate through the data we retrieved from the JSON file
        print(f"json_data[2]: {len(json_data[2])}")

        for row in json_data[2]:
            # Get the basic data from the row and put it into the correct variables
            row_date = row["date"]
            row_trackingnumber = row["tracking_number"]
            row_cargoweight = row["cargo_weight"]
            row_distancenaut = row["distance_naut"]
            row_durationhours = row["duration_hours"]
            row_averagespeed = row["average_speed"]

            # Get the data for which we need to go a little bit further into the data
            row_origin = row["origin"]
            row_destination = row["destination"]
            row_vessel = row["vessel"]

            # Import the data from the rows: Origin, Destination and Vessel.
            # If the data for these is already known, then we just return their current ID from the database
            # Else we insert the data and return their newly created ID
            import_data_port(db_conn, row_origin)
            import_data_port(db_conn, row_destination)
            import_data_vessel(db_conn, row_vessel)

            # Insert the shipment itself into the database
            internal_shipment_id = db_insert_shipment(db_conn, row_trackingnumber, row_date, row_cargoweight,
                                                      row_distancenaut, row_durationhours, row_averagespeed,
                                                      row["origin"]["id"], row["destination"]["id"],
                                                      row["vessel"]["imo"])

            temp_list_internal_shipment_ids.append(internal_shipment_id)

        # Check if the amount of internal_shipment_id's is the same as the amount of records
        if len(json_data[2]) == len(temp_list_internal_shipment_ids):
            # Commit the inserts to the database
            db_conn.commit()
            # Update the return result to display that the data has been commited to the database
            return_result[0] = True

    # Send back the result of the import
    return return_result


def import_data_port(db_connection, port_info: dict) -> str:
    # Retrieve all the required data from the dict and put it into the correct variables for these
    port_id = port_info["id"]
    port_code = port_info["code"]
    port_name = port_info["name"]
    port_city = port_info["city"]
    port_province = port_info["province"]
    port_country = port_info["country"]

    # Search the database to see if there is already a port with the same id, if so return its id
    search_result = db_search_port(db_connection, port_id)
    # Check if the port is found
    if search_result[0]:
        return search_result[1]
    else:
        insert_result = db_insert_port(db_connection, port_id, port_code, port_name,
                                       port_city, port_province, port_country)
        if insert_result[0]:
            return insert_result[1]
        else:
            return "-999999"


# This function will import the data for the vessel
def import_data_vessel(db_connection, vessel_info: dict) -> int:
    # Retrieve all the required data from the dict and put it into the correct variables for these
    vessel_imo = vessel_info["imo"]
    vessel_mmsi = vessel_info["mmsi"]
    vessel_country = vessel_info["country"]
    vessel_name = vessel_info["name"]
    vessel_type = vessel_info["type"]
    vessel_build = vessel_info["build"]
    vessel_gross = vessel_info["gross"]
    vessel_netto = vessel_info["netto"]
    vessel_length = vessel_info["size"].replace(" ", "").split("/")[0]
    vessel_beam = vessel_info["size"].replace(" ", "").split("/")[1]

    # Search the database to see if there is already a port with the same id, if so return its id
    search_result = db_search_vessel(db_connection, vessel_imo)
    # Check if the port is found
    if search_result[0]:
        return search_result[1]
    else:
        insert_result = db_insert_vessel(db_connection, vessel_imo, vessel_mmsi, vessel_name,
                                         vessel_country, vessel_type, vessel_build,
                                         vessel_gross, vessel_netto, vessel_length, vessel_beam)
        if insert_result[0]:
            return insert_result[1]
        else:
            return "-999999"


# This function will check if all the required tables exist and if they don't, will automatically create them
def db_check_tables():
    pass


# This function will search the database to see if the port already exists
def db_search_port(db_conn, port_id) -> [bool, str]:
    query = "SELECT ID FROM ports WHERE ID = ?"
    cur = db_conn.execute(query, [port_id])
    result = cur.fetchone()
    if result is not None:
        return [True, result]
    else:
        return [False, "Port not found"]


def db_search_vessel(db_conn, vessel_imo) -> [bool, str]:
    query = "SELECT imo FROM vessels WHERE imo = ?"
    cur = db_conn.execute(query, [vessel_imo])
    result = cur.fetchone()
    if result is not None:
        return [True, result]
    else:
        return [False, "Port not found"]


# This function will insert a new port into the database
def db_insert_port(db_conn, port_id: str, port_code: int, port_name: str, port_city: str, port_province: str,
                   port_country: str) -> [bool, str]:
    # Preform the query in a Try-Except to handle errors when inserting data
    # Any errors are reported back to the function that called this function so that we can
    # get an overview of all the errors
    try:
        # Create the insert query
        query = "INSERT INTO ports (id, code, name, city, province, country) VALUES (?, ?, ?, ?, ?, ?)"
        # Execute the query and get the cursor
        cur = db_conn.execute(query, [port_id, port_code, port_name, port_city, port_province, port_country])
        # Get the ID of the last row we inserted
        insert_id = cur.lastrowid
        # Return a True when we did the insert and return it with the ID of our insert
        return [True, insert_id]
    except Exception as e:
        # If there was any error when inserting,
        # then pass a False back with the error for later display back to the user
        return [False, -999999, str(e)]


# This function will insert a vessel into the database
def db_insert_vessel(db_conn, vessel_imo, vessel_mmsi, vessel_name, vessel_country, vessel_type, vessel_build,
                     vessel_gross, vessel_netto, vessel_length, vessel_beams) -> [bool, str]:
    # Preform the query in a Try-Except to handle errors when inserting data
    # Any errors are reported back to the function that called this function so that we can
    # get an overview of all the errors
    try:
        # Create the insert query
        query = ("INSERT INTO vessels (imo, mmsi, name, country, type, build, gross, netto, length, beam) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
        # Execute the query and get the cursor
        cur = db_conn.execute(query, [vessel_imo, vessel_mmsi, vessel_name, vessel_country, vessel_type, vessel_build,
                                      vessel_gross, vessel_netto, vessel_length, vessel_beams])
        # Get the ID of the last row we inserted
        insert_id = cur.lastrowid
        # Return a True when we did the insert and return it with the ID of our insert
        return [True, insert_id]
    except Exception as e:
        # If there was any error when inserting,
        # then pass a False back with the error for later display back to the user
        return [False, -999999, str(e)]


# This function will insert a shipment into the database
def db_insert_shipment(db_conn, shipment_trackingnumber, shipment_date, shipment_cargoweight, shipment_distancenaut,
                       shipment_durationhours, shipment_averagespeed, origin_internal_id, destination_internal_id,
                       vessel_internal_id) -> [bool, int]:
    # Preform the query in a Try-Except to handle errors when inserting data
    # Any errors are reported back to the function that called this function so that we can
    # get an overview of all the errors
    try:
        # Create the insert query
        query = ("INSERT INTO shipments (id, date, cargo_weight, distance_naut, duration_hours, "
                 "average_speed, origin, destination, vessel) "
                 "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
        # Execute the query and get the cursor
        cur = db_conn.execute(query, [shipment_trackingnumber, shipment_date, shipment_cargoweight,
                                      shipment_distancenaut, shipment_durationhours, shipment_averagespeed,
                                      origin_internal_id, destination_internal_id, vessel_internal_id])
        # Get the ID of the last row we inserted
        insert_id = cur.lastrowid
        # Return a True when we did the insert and return it with the ID of our insert
        return [True, insert_id]
    except Exception as e:
        # If there was any error when inserting,
        # then pass a False back with the error for later display back to the user
        return [False, -999999, str(e)]


if __name__ == "__main__":
    # Turn this on to use the interface
    # # This function will check if the database exists,
    # # and will if not create the database file and all the required tables needed
    # db_check_tables()
    # # This function is for the main part of this application
    # main()

    # Use this when running in codegrade
    import_data("shipments.json")
