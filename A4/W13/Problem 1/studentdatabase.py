# Import the required modules
import os
import sys
import sqlite3

# Define a variable which will store our database filename
db_file = 'studentdatabase.db'


def db_connect():
    con = sqlite3.connect(os.path.join(sys.path[0], db_file))
    return con


def db_close(con):
    return con.close()


def db_table_students_check():
    try:
        con = db_connect()
        con.execute(
            '''CREATE TABLE IF NOT EXISTS students (
                studentnumber INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                city TEXT NOT NULL,
                date_of_birth DATE NOT NULL,
                class TEXT DEFAULT NULL 
            );'''
        )
        return True
    except sqlite3.OperationalError:
        return False


def db_insert_student(first_name, last_name, city, date_of_birth, school_class):
    # Prepare a SQL statement
    insert_query = "INSERT INTO students (first_name, last_name, city, date_of_birth, class) VALUES (?, ?, ?, ?, ?)"

    # Connect to the database
    con = db_connect()
    # Execute the query
    studentnumber = con.execute(insert_query, [first_name, last_name, city, date_of_birth, school_class]).lastrowid
    # Commit the insert
    con.commit()
    # Close the database connection
    db_close(con)

    return studentnumber


def db_update_student(studentnumber, school_class):
    try:
        # Prepare a SQL statement
        insert_query = "UPDATE students SET class = ? WHERE studentnumber = ?;"

        # Connect to the database
        con = db_connect()
        # Execute the query
        rows_affected = con.execute(insert_query, [school_class, studentnumber])
        print(rows_affected)
        if len(rows_affected) > 0:
            # Commit the insert
            con.commit()
            # Close the database connection
            db_close(con)
            # Return a succes message
            return f"succes, student with studentnumber: {studentnumber} has been updated"
        else:
            # Close the database connection
            db_close(con)
            return f"Could not find student with number: {studentnumber}"
    except sqlite3.OperationalError:
        return f"Could not find student with number: {studentnumber}"


def print_menu():
    print("[A] Add new student")
    print("[C] Assign student to class")
    print("[D] List all students")
    print("[L] List all students in class")
    print("[S] Search student")
    print("[Q] Quit program")


def add_student():
    input_firstname = input("Enter student first name: ")
    input_lastname = input("Enter student last name: ")
    input_city = input("Enter the current city where the student resides: ")
    input_date_of_birth = input("Enter student date of birth: ")
    input_school_class = input("(optional) Enter student class: ")

    if input_school_class == "":
        input_school_class = None

    print(f"Student inserted into database, Assigned student number: {db_insert_student(input_firstname, input_lastname, input_city, input_date_of_birth, input_school_class)}")


def update_student():
    input_studentnumber = input("Enter student number: ")
    input_schoolclass = input("Enter student class: ")

    print(db_update_student(input_studentnumber, input_schoolclass))


def main():
    if db_table_students_check():
        while True:
            print_menu()
            input_option = input("Please select an option: ").upper()
            if input_option == "A":
                add_student()
            elif input_option == "C":
                update_student()
            elif input_option == "D":
                pass
            elif input_option == "L":
                pass
            elif input_option == "S":
                pass
            elif input_option == "Q":
                print("Exiting program, Thank you for using this program. See you next time!")
                break
            else:
                print("Invalid input, Please select an valid option")


if __name__ == "__main__":
    main()
