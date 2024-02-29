import sqlite3
import os

def_options = ["Create", "Read", "Update", "Delete"]
def_options_explanation = ["Create a new record", "Read all the records", "Update a record", "Delete a record"]
shutdown_bool = False
firsttime_use = True


def print_menu():
    # Print the menu header
    print("\n Program options")

    # Get the size of the largest size of the command words
    max_word_len = 0
    for i in def_options:
        word_len = len(i)
        if word_len > max_word_len:
            max_word_len = word_len

    # make a list with all the options
    max_command_len = 0
    list_options_and_explanations = []
    pos = 0
    for i in def_options:
        word_len = len(i)
        spaces_needed = max_word_len - word_len

        spaces = ""
        while spaces_needed > len(spaces):
            spaces += " "

        command_row = f"{i}{spaces} - {def_options_explanation[pos]}"

        list_options_and_explanations += [command_row]

        if len(command_row) > max_command_len:
            max_command_len = len(command_row)

        # Move the position
        pos += 1

    # Generate the underscore line based on the max length of the command + it's explanation
    header_underscore_line = ""
    while max_command_len > len(header_underscore_line):
        header_underscore_line += "-"
    # Print the just generated header underscore line
    print(header_underscore_line)

    # Print the command options list
    for i in list_options_and_explanations:
        print(i)

    body_underscore_line = ""
    while max_command_len > len(body_underscore_line):
        body_underscore_line += "-"
    # Print the just generated header underscore line
    print(body_underscore_line + "\n")


def db_check():
    global shutdown_bool
    db_works = False

    # Try and see if the file is there. if it's not there then we generate the file
    if os.path.isfile('sqlite.db'):
        conn_test_result = db_conn_test()
        if conn_test_result:
            print("Database connection has been established")
    else:
        print('File does not exist')
        print('Generating a new database file')
        try:
            os.mknod('sqlite.db')
            conn_test_result = db_conn_test()
            if conn_test_result:
                print("Database connection has been established 1")
        except ValueError:
            print("Database connection could not be established")
            print(ValueError)



    # def db_create():
    # Open a connection to the SQLite database
    con = sqlite3.connect("sqlite.db")


def db_conn_test():
    global shutdown_bool

    try:
        conn = sqlite3.connect('sqlite.db')
        conn.close()
        return True
    except sqlite3.OperationalError:
        print("The program has run into a unexpected SQLite database error")
        print("---------------------------------------------------------------------------------------------")
        print("SQLite Database error: \n")
        print(sqlite3.OperationalError + "\n")
        print("---------------------------------------------------------------------------------------------")
        print("Removing database file and generating a new one")

        os.remove('sqlite.db')
        os.mknod('sqlite.db')

        print("New database file generated, Preforming connection test")
        conn_tries = 1
        conn_succes = False
        while conn_succes != True or range(3):
            print(f"SQLite database file connection attempt: {conn_tries}")

            try:
                conn = sqlite3.connect('sqlite.db')
                conn.close()
                conn_succes = True
            except sqlite3.OperationalError:
                print("Connection failed, trying again")

        if not conn_succes:
            print("Critical error: Database connection could not be established"
                  "even after generating a new database file.")
            print("Shutting down program...")
            shutdown_bool = True

        return True

# def db_read():

# def db_update():

# def db_delete():

# def db_get_latest():


while not shutdown_bool:
    valid_input = False
    while not valid_input:
        if firsttime_use:
            db_check()
            print("Welcome to the Teaching example for Databases")
            firsttime_use = False

        input_usr_response = input("What would you like to do: ")

        if input_usr_response == "Help":
            print_menu()
        elif input_usr_response in def_options:
            print("nothing")
        else:
            print("Invalid input, pleases input a valid response")
