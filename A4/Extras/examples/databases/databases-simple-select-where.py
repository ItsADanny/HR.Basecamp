# Import the required module for connecting to our SQLite database
import sqlite3

if __name__ == '__main__':
    # Connect to the database
    school = sqlite3.connect("school.sqlite")

    # Create an SQL Query
    query = "SELECT name, date_of_birth FROM students WHERE city = \"Utrecht\""

    # Execute the Query and assign the results to a variable
    students = school.execute(query)

    # Loop through the results and print the individual results
    for student in students:
        print(student)

    # Close the database connection
    school.close()