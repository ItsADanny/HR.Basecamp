# Import the required modules
import json

def list_menu():
    print("[L] List contacts")
    print("[A] Add contact")
    print("[R] Remove contact")
    print("[M] Merge contacts")
    print("[Q] Quit program\n\n")


# Here we store all the menu item functions
# ---------------------------------------------------------------------------------------------------------------
def list_contacts():
    pass


# This function will be called when the user wants to add a contact
def add_contact():
    required_information = ["Firstname", "Lastname", "Emails", "Phonenumbers"]
    input_information = []
    for i in required_information:
        valid = False
        while not valid:
            input_user = input(f"{i}: ")

            if i == "Firstname" or i == "Lastname":
                # Preform a check to see if the given Firstname or Lastname is valid, if so set the valid variable to True
                valid = name_check(input_user)
            if i == "Emails":
                # Prefrom a check to see if the given E-mail is valid, if so set the valid variable to True
                valid_list = email_check(input_user)

                invalids = 0

                for e in valid_list:
                    if not e:
                        invalids += 1

                if invalids == 0:
                    valid = True

            if i == "Phonenumbers":
                # Preform a check to see if the given Phonenumbers are valid, if so set the valid variable to True
                valid = phone_check(input_user)

            if valid:
                input_information.append(input_user)
            else:
                print(f"Invalid {i}, Please use a valid {i}")

def remove_contact():
    pass


def merge_contact():
    pass


# Here we store all the check functions
# ---------------------------------------------------------------------------------------------------------------
"""
Add a contact with first name and last name (only alphabet)
multiple (unique)
e-mails (containing at least one '@')
multiple (unique)
phone numbers (only digits)
"""

# This function checks if the input from the user is a valid First- or Last- name
def name_check(usr_input):
    if usr_input.isalpha():
        return True
    else:
        return False


# This function checks if the input from the user is a valid E-mailadres
def email_check(usr_input):
    # Email can be multiple
    replaced_usr_input = usr_input.replace(" ", "")
    splitted_usr_input = replaced_usr_input.split(",")

    valid_emails = []

    for i in splitted_usr_input:
        valid_email = False
        for j in i:
            if not valid_email:
                if j == "@":
                    valid_email = True

        valid_emails.append(valid_email)

    return valid_emails


# This function checks if the input from the user is a valid
def phone_check(usr_input):


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
            merge_contact()
        elif input_userchoice.lower() == "q":
            print("Exiting program")
            break
        else:
            print("Invalid input, Please enter a valid input")


# Run the program function when the .py file has been started
program()
