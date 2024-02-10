__author__ = 'Danny de Snoo, HR-nr: 1091749'

# import the datetime and timedelta from the datetime module
from datetime import datetime
from datetime import timedelta

# Request an input from the user, and describe that you want a date as its input
input_date = input("Input Date: ")

# define the datetime format you only want to accept
def_datetime_format = "%Y-%m-%d"

# create a variable that will be used as a boolean to see if the given datetime input
# from the user was in the correct format
boolean_dateformat_check = True

# Run the format test in a try-except to see if the given input was correct
try:
    boolean_dateformat_check = bool(datetime.strptime(input_date, def_datetime_format))
except ValueError:
    boolean_dateformat_check = False

# Check if the input was correct or not
if boolean_dateformat_check:
    # if the date is in the correct format, then go further in executing the program
    # Turn the date into a datetime object
    datetime_date = datetime.strptime(input_date, def_datetime_format)

    # Add 1 day onto the date
    datetime_finaldate = datetime_date + timedelta(days=1)

    # Print the result
    print(f"Next Date: {datetime_finaldate}")
else:
    # if the date isn't entered in a valid format, then print this error message
    print("Input format ERROR. Correct Format: YYYY-MM-DD")
