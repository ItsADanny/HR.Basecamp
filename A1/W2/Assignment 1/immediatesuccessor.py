__author__ = 'Danny de Snoo, HR-nr: 1091749'

# Define a list of invalid characters
def_invalid_characters = ["/", "_", ".", ",", "|"]

# Request an input from the user
input_date = input()

# Check if the string contains any characters that are not allowed
if any(x in input_date for x in def_invalid_characters):
    print("Error: Correct Format: YYYY-MM-DD")
else:
    # If there aren't any foreign characters in the string continue preforming the check

    # Check if the input can be split into 3 parts
    if len(input_date.split("-")) == 3:
        # If it can be split, continue the check
        separated_input_date = input_date.split("-")

        # Check if all the separated parts are the correct length
        date_year = int(separated_input_date[0])
        date_month = int(separated_input_date[1])
        date_day = int(separated_input_date[2])

        # Check if the year is the correct length
        if len(str(date_year)) == 4:
            # Check if the month is a valid month
            if 0 < int(date_month) <= 12:
                if date_month == 2:
                    date_valid = False

                    # Check if February doesn't have a value greater than 28, if so give an error message
                    if int(date_day) > 28:
                        date_valid = False
                    # Check if the day given is the last day of February
                    elif int(date_day) == 28:
                        # If so set the month to next month and set the day to the first day of the month
                        date_month = 3
                        date_day = 1
                        date_valid = True
                    else:
                        # Else add 1 day
                        date_day += 1
                        date_valid = True

                    if date_valid:
                        if len(str(date_month)) == 1:
                            date_month = f"0{date_month}"

                        if len(str(date_day)) == 1:
                            date_day = f"0{date_day}"

                        print(f"Next Date: {date_year}-{date_month}-{date_day}")
                    else:
                        print("input format ERROR. Correct Format: YYYY-MM-DD")

                elif int(date_month) == 12:
                    date_valid = False

                    # Check if the day is the last day of the month December
                    if int(date_day) == 31:
                        # If so then set the new date to the following year
                        date_year += 1
                        date_month = 1
                        date_day = 1
                        date_valid = True
                    else:
                        # else add 1 day
                        date_day += 1
                        date_valid = True

                    if date_valid:
                        if len(str(date_month)) == 1:
                            date_month = f"0{date_month}"

                        if len(str(date_day)) == 1:
                            date_day = f"0{date_day}"

                        print(f"Next Date: {date_year}-{date_month}-{date_day}")
                    else:
                        print("input format ERROR. Correct Format: YYYY-MM-DD")
                else:
                    date_valid = False

                    # Check if the integer can be divided
                    if int(date_month) % 2:
                        # If so then the max date for that month is 30
                        if int(date_day) > 30:
                            date_valid = False
                        elif int(date_day) == 30:
                            # If it's the last day of the month, add 1 to the month and
                            # set the day to the first day of the next month
                            date_month += 1
                            date_day = 1
                            date_valid = True
                        else:
                            # else add 1 day
                            date_day += 1
                            date_valid = True
                    else:
                        # Else the max date for the month is 31
                        if int(date_day) > 31:
                            date_valid = False
                        elif int(date_day) == 31:
                            # If it's the last day of the month, add 1 to the month and
                            # set the day to the first day of the next month
                            date_month += 1
                            date_day = 1
                            date_valid = True
                        else:
                            # else add 1 day
                            date_day += 1
                            date_valid = True

                    if date_valid:
                        if len(str(date_month)) == 1:
                            date_month = f"0{date_month}"

                        if len(str(date_day)) == 1:
                            date_day = f"0{date_day}"

                        print(f"Next Date: {date_year}-{date_month}-{date_day}")
                    else:
                        print("input format ERROR. Correct Format: YYYY-MM-DD")
            else:
                print("input format ERROR. Correct Format: YYYY-MM-DD")
        else:
            print("input format ERROR. Correct Format: YYYY-MM-DD")
    else:
        # If not end the program
        print("input format ERROR. Correct Format: YYYY-MM-DD")
