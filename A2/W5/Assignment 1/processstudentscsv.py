# Import the required modules
import os
import sys

# Create two lists that will store our valid and invalid lines
valid_lines = []
corrupt_lines = []

# Create a list with all the allowed studies
allowed_studies = ["INF", "TINF", "CMD", "AI"]


# This function checks if the student number is valid
def studentnumber_check(studentnumber):
    # Predefine our return value
    return_value = False

    # Preform the check to see if it is 7 long
    if len(studentnumber) == 7:
        # Preform the check to see if it starts with a 0
        if studentnumber[0] == "0":
            # Preform the check to see if it's second character is a 9 or 8
            if studentnumber[1] == "9" or studentnumber[1] == "8":
                return_value = True

    # Return the result
    return return_value


# This function checks if the name is valid
def studentname_check(name):
    # Predefine our return value
    return_value = False

    # Preform the check to see if it is only alpha characters (with spaces remove ofcourse)
    if name.replace(" ", "").isalpha():
        return_value = True

    # Return the result
    return return_value


# This function checks if the date of birth is valid
def studentbirthdate_check(date):
    # Predefine our return value
    return_value = False

    # Preform a check to see if the right date format has been used
    if date[4] == "-" and date[7] == "-":
        # split the
        splitted_date = date.split("-")

        # Create a valid_parts integer which will start at 0 to see if all parts are valid
        valid_parts = 0

        # Year check
        # ------------------------------------
        # check to see if the number is 4 long and if its numeric
        if len(splitted_date[0]) == 4 and splitted_date[0].isnumeric():
            # Check to see if the year is between 1960 and 2004
            if 1960 <= int(splitted_date[0]) <= 2004:
                valid_parts += 1

        # Month check
        # ------------------------------------
        # check to see if the number is 2 long and if its numeric
        if len(splitted_date[1]) == 2 and splitted_date[1].isnumeric():
            # Check to see if the month is between the 1 and 12:
            if 1 <= int(splitted_date[1]) <= 12:
                valid_parts += 1

        # Day check
        # ------------------------------------
        # check to see if the number between the 1 and 2 long and if its numeric
        if 1 <= len(splitted_date[1]) <= 2 and splitted_date[2].isnumeric():
            # Check to see if the day is between the 1 and 12:
            if 1 <= int(splitted_date[2]) <= 31:
                valid_parts += 1

        # Check to see if al parts were valid integers
        if valid_parts == 3:
            return_value = True

    # Return the result
    return return_value


# This function will check the student's study program
def studentstudyprogram_check(study):
    # Predefine our return value
    return_value = False

    # Check if the study is one of the allowed studies
    for allowed_study in allowed_studies:
        # Check if the study matches one of the allowed studies
        if allowed_study == study:
            # Update the return value if so
            return_value = True

    # Return the result
    return return_value


def validate_data(line):
    # Make it possible to use the global lists
    global corrupt_lines, valid_lines

    # We split the line into its seperate parts
    split_line = line.split(",")
    # Retrieve the data from our list which contains all the data line seperated
    student_studentnumber = split_line[0]
    student_firstname = split_line[1]
    student_lastname = split_line[2]
    student_birthdate = split_line[3]
    student_studyprogram = split_line[4]

    # Create a list in which we will store the invalid parts
    # (This will also be used to check if it's a fully valid line later.)
    invalid_parts = list()

    # Check the data from the line
    # If a parts invalid. Add it to the list with invalid parts for that line
    if not studentnumber_check(student_studentnumber):
        invalid_parts += [f"{student_studentnumber}"]
    if not studentname_check(student_firstname):
        invalid_parts += [f"{student_firstname}"]
    if not studentname_check(student_lastname):
        invalid_parts += [f"{student_lastname}"]
    if not studentbirthdate_check(student_birthdate):
        invalid_parts += [f"{student_birthdate}"]
    if not studentstudyprogram_check(student_studyprogram):
        invalid_parts += [f"{student_studyprogram}"]

    if len(invalid_parts) > 0:
        corrupt_lines.append(f"{line} => INVALID DATA: {invalid_parts}")
    else:
        valid_lines.append(line)


def main(csv_file):
    with open(os.path.join(sys.path[0], csv_file), newline='') as csv_file:
        # skip header line
        next(csv_file)

        for line in csv_file:
            validate_data(line.strip())

    print('### VALID LINES ###')
    print("\n".join(valid_lines))
    print('### CORRUPT LINES ###')
    print("\n".join(corrupt_lines))


if __name__ == "__main__":
    main('students.csv')
