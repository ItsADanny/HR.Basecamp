# Import the required modules
import json

filename = "contacts.json"


# Here we store the functions that interact directly with the JSON file
# ---------------------------------------------------------------------------------------------------------------
def load_json() -> dict:
    # Open the file
    file = open(filename, "r")
    # Return the JSON object as a Dict
    data = json.load(file)
    # Close the file
    file.close()

    # Return the iterable data
    return data


def append_json(data: str) -> bool:
    # Here we use a Try, Expect block to return a true or false if the appending was succesfull
    try:
        # Open the file
        file = open(filename, "r+")
        # Load the json file
        json_file = json.load(file)
        # Join the current data and new data together
        json_file.append(data)
        # Set the file seek position
        file.seek(0)
        # convert the data back to JSON
        json.dump(json_file, file, indent=4)
        # Close the file
        file.close()

        return True
    except FileNotFoundError as error:
        print(f"FILE_NOT_FOUND_ERROR: {error}")
        return False
    except json.decoder.JSONDecodeError as error:
        print(f"JSON_DECODER_ERROR: {error}")
        return False


def write_json(data: str) -> bool:
    # Here we use a Try, Expect block to return a true or false if the writing was succesfull
    try:
        # Open the file
        file = open(filename, "w")
        # Set the file seek position
        file.seek(0)
        # convert the data back to JSON
        json.dump(data, file, indent=4)
        # Close the file
        file.close()

        return True
    except FileNotFoundError as error:
        print(f"FILE_NOT_FOUND_ERROR: {error}")
        return False
    except json.decoder.JSONDecodeError as error:
        print(f"JSON_DECODER_ERROR: {error}")
        return False


# Here we store all the menu item functions
# ---------------------------------------------------------------------------------------------------------------
def list_contacts():
    # Get the JSON data
    data = load_json()

    # Iterate through the data
    for line in data:
        # Retrieve the data and put it into the correct variable
        contact_id = line["id"]
        contact_firstname = line["first_name"]
        contact_lastname = line["last_name"]
        list_contact_emails = line["emails"]
        list_contact_phones = line["phone_numbers"]
        # Create 2 empty variables in which we will store the emails and phones in the way we will display it
        contact_emails = ""
        contact_phones = ""

        # Loop through the list object and put the emails into the variable for display
        for email in list_contact_emails:
            if contact_emails == "":
                contact_emails = email
            else:
                contact_emails += f", {email}"

        # Loop through the list object and put the phones into the variable for display
        for phone in list_contact_phones:
            if contact_phones == "":
                contact_phones = phone
            else:
                contact_phones += f", {phone}"

        # Print the result
        print("======================================")
        print(f"Position:  {contact_id}")
        print(f"First name:  {contact_firstname}")
        print(f"Last name:  {contact_lastname}")
        print(f"Emails:  {contact_emails}")
        print(f"Phone numbers:  {contact_phones}")


# This function will be called when the user wants to add a contact
def add_contact():
    # Create 4 Empty variables in which we will store the Firstname, Lastname, Emails and Phonenumbers
    user_firstname = ""
    user_lastname = ""
    user_emails = []
    user_phones = []

    # Loop until you get a valid First name
    while True:
        input_firstname = input("Firstname: ")
        if name_check(input_firstname):
            user_firstname = input_firstname
            break

    # Loop until you get a valid First name
    while True:
        input_lastname = input("Lastname: ")
        if name_check(input_lastname):
            user_lastname = input_lastname
            break

    # Loop until you get a valid email(s)
    while True:
        input_email = input("Email(s): ")
        if email_check(input_email):
            user_emails = string_to_list(input_email)
            break

    # Loop until you get a valid phonenumber(s)
    while True:
        input_phones = input("Phonenumber(s): ")
        if phone_check(input_phones):
            user_phones = string_to_list(input_phones)
            break

    new_id = get_highest_id() + 1

    new_json_contact = {
        "id": new_id,
        "first_name": user_firstname,
        "last_name": user_lastname,
        "emails": user_emails,
        "phone_numbers": user_phones
    }

    # Write the new data
    if append_json(new_json_contact):
        print(f"Contact [{user_firstname} {user_lastname}] has been successfully added")
    else:
        print(f"Contact [{user_firstname} {user_lastname}] could not be added")


def remove_contact():
    # Predefine a variable in which we will store the valid select position by the user
    user_selected_position = 0

    # Loop until we get a valid position (ID)
    while True:
        input_position = input("Position (ID): ")
        # Check to see if the input is an integer
        if input_position.isnumeric():
            # Check to see if the position does exist in the JSON file
            if does_position_exist(int(input_position)):
                # Declare it as the selected position and break out of the loop
                user_selected_position = input_position
                break

    if purge_position(user_selected_position):
        print(f"Position [{user_selected_position}] successfully removed")
    else:
        print(f"Position [{user_selected_position}] could not be removed")


def merge_contacts():
    # Create a dict in which we will store the occurrences of users
    dict_user_occurrences = dict()

    # Iterate through the data
    for line in load_json():
        # Retrieve the First and Lastname and put it into a fullname variable
        contact_fullname = f"{line["first_name"]} {line["last_name"]}"

        # Check if the fullname of the contact has already been added to our dict,
        # if not add him with a 1 else update it with 1
        if contact_fullname not in dict_user_occurrences:
            dict_user_occurrences[contact_fullname] = 1
        else:
            dict_user_occurrences[contact_fullname] += 1

    # Loop through our dict
    for key in dict_user_occurrences:
        # If the user has more than 1 occurrence, then we know that we must merge this contact
        if dict_user_occurrences[key] > 1:
            # Retrieve the highest ID of the contact with selected fullname
            highest_id = get_highest_id_fullname(key)

            # Create two variables that will store the emails and phonenumbers
            duplicate_contact_emails = list()
            duplicate_contact_phonenumbers = list()

            # Iterate through the data
            for line in load_json():
                # Retrieve the ID and fullname from the current line
                contact_id = line["id"]
                contact_fullname = f"{line["first_name"]} {line["last_name"]}"
                # Check to see if the contact_fullname and key match,
                # and check to see if this isn't the highest id of this contact
                if contact_fullname == key and contact_id != highest_id:
                    # Put the duplicate contacts emails and phonenumbers into the two designated variables
                    # and purge the duplicate contact
                    duplicate_contact_emails.append(line["emails"])
                    duplicate_contact_phonenumbers.append(line["phone_numbers"])
                    # Purge the duplicate contact
                    purge_position(contact_id)

            # Create a variable in which we will store our new JSON file data
            json_file_data = list()

            # Now loop one more time through the lines
            # and update the last remaining version of the contact with the duplicate contacts emails and phonenumbers
            for line in load_json():
                if f"{line["first_name"]} {line["last_name"]}" == key and line["id"] == highest_id:
                    contact_emails = line["emails"]
                    contact_phonenumbers = line["phone_numbers"]
                    for duplicate_email_line in duplicate_contact_emails:
                        for email in duplicate_email_line:
                            contact_emails.append(email)
                    for duplicate_phonenumber_line in duplicate_contact_phonenumbers:
                        for phonenumber in duplicate_phonenumber_line:
                            contact_phonenumbers.append(phonenumber)

                    update_contact_line = {"id": line["id"],
                                           "first_name": line["first_name"],
                                           "last_name": line["last_name"],
                                           "emails": contact_emails,
                                           "phone_numbers": contact_phonenumbers}
                    # Append the new dict in the place of the old contact version
                    json_file_data.append(update_contact_line)
                else:
                    # Append the contact if its not the selected contact
                    json_file_data.append(line)

            # Write the new JSON data to the JSON file
            write_json(json_file_data)

    # Print a success message
    print("All possible contacts have been merged")


# Here we store all the check functions
# ---------------------------------------------------------------------------------------------------------------
# This function checks if the input from the user is a valid Firstname or Lastname
def name_check(usr_input: str) -> bool:
    # Set the return value default to False
    return_result = False

    # First, remove the spaces to see if all the characters are alpha characters
    usr_input = usr_input.replace(" ", "")
    # Then check if the usr_input only contains alpha characters, If so set the return value to True
    if usr_input.isalpha():
        return_result = True

    # Return the result
    return return_result


# This function checks if the input from the user is a valid E-mailadres
def email_check(usr_input: str) -> bool:
    print(usr_input)

    # First, Create a variable in which we will store the valid amount of inputted email-addresses
    # and a variable to store the return value
    valid_emails = 0
    return_result = False
    # Second, turn the input string into a list
    list_usr_input = string_to_list(usr_input)

    print(list_usr_input)

    # Third, iterate through the list
    for item in list_usr_input:
        # Create a variable in which we will store a control boolean for the @ character
        contains_at = False
        # Create a variable that will check if the emails that were given are unique
        unique_emails = False

        # Third check to see if the string in the list contains a @, if so set the contains_at to True
        for char in item:
            if char == "@":
                contains_at = True

        # Loop through the inputted mails and see how many occurrences are made of the current mail
        occurrences = 0
        for mail in list_usr_input:
            if item == mail:
                occurrences += 1
        # Check if there was only 1 occurrence of the email in the input list
        if occurrences == 1:
            unique_emails = True

        # Check if both requirements are met
        if contains_at and unique_emails:
            valid_emails += 1

    # Check to see if the amount of valid emails is the same as the inputted amount, set the return value to True
    if valid_emails == len(list_usr_input):
        return_result = True

    # Return the result
    return return_result


# This function checks if the input from the user is a valid phone number
def phone_check(usr_input: str) -> bool:
    # First, Create a variable in which we will store the valid amount of inputted email-addresses
    # and a variable to store the return value
    valid_phones = 0
    return_result = False
    # Second, turn the input string into a list
    list_usr_input = string_to_list(usr_input)
    # Third, iterate through the list
    for item in list_usr_input:
        item = item.replace("-", "")

        if item.isnumeric():
            valid_phones += 1

    if valid_phones == len(list_usr_input):
        return_result = True

    return return_result


# Here we store some program functions
# ---------------------------------------------------------------------------------------------------------------
# This function will turn a string into a list
def string_to_list(string: str) -> list:
    # First, Create an empty return list object
    return_list = list()
    # Second, we split up the string
    splitted_string = string.split(",")
    # Third, we clean the results (Removing whitespaces and blank spaces in front and back of the items)
    # and add them to the return list
    for item in splitted_string:
        item = item.strip()
        return_list.append(item)

    # Return the results
    return return_list


# This function will return the highest ID stored in the JSON file
def get_highest_id() -> int:
    # Declare the return_value variable and set it to 0
    return_value = 0

    # Get the JSON data
    data = load_json()

    # Iterate through the data
    for line in data:
        # Retrieve the data and put it into the correct variable
        contact_id = int(line["id"])
        # Check to see if the current id is higher than the previous highest
        if contact_id > return_value:
            return_value = contact_id

    # Return the result
    return return_value


# This function will return the highest ID based on fullname
def get_highest_id_fullname(fullname: str) -> int:
    # Declare the return_value variable and set it to 0
    return_value = 0

    # Get the JSON data
    data = load_json()

    # Iterate through the data
    for line in data:
        # Retrieve the data and put it into the correct variable
        contact_id = int(line["id"])
        contact_fullname = f"{line["first_name"]} {line["last_name"]}"
        # Check to see if the current id is higher than the previous highest
        # and if the fullname from the json is the same as the selected fullname
        if contact_id > return_value and contact_fullname == fullname:
            return_value = contact_id

    # Return the result
    return return_value


# This function will return a boolean based on if an inputted position exists
def does_position_exist(position: int) -> bool:
    does_exist = False

    # Get the JSON data
    data = load_json()

    # Iterate through the data
    for line in data:
        # Retrieve the data and put it into the correct variable
        contact_id = int(line["id"])

        # Check to see if the position (ID) exists
        if contact_id == position:
            does_exist = True

    # Return the result
    return does_exist


def purge_position(position: int) -> bool:
    # Create a new list variable in which we will store our data without the position that has been marked for removal
    processed_data = list()

    # Get the JSON data
    data = load_json()

    # Iterate through the data
    for line in data:
        # Retrieve the data and put it into the correct variable
        contact_id = int(line["id"])

        if int(contact_id) != int(position):
            # append the line if it's not the position that has been designated for termination
            processed_data.append(line)

    if write_json(processed_data):
        return True
    else:
        return False


# Function that will display the option list
def list_menu():
    print("[L] List contacts")
    print("[A] Add contact")
    print("[R] Remove contact")
    print("[M] Merge contacts")
    print("[Q] Quit program\n\n")


# Here we store the main program
# ---------------------------------------------------------------------------------------------------------------
def program():
    while True:
        list_menu()
        input_userchoice = input("Enter your choice: ")
        if input_userchoice.lower() == "l":
            list_contacts()
        elif input_userchoice.lower() == "a":
            add_contact()
        elif input_userchoice.lower() == "r":
            remove_contact()
        elif input_userchoice.lower() == "m":
            merge_contacts()
        elif input_userchoice.lower() == "q":
            print("Exiting program")
            break
        else:
            print("Invalid input, Please enter a valid input")


# Run the program function when the .py file has been started
if __name__ == "__main__":
    program()
