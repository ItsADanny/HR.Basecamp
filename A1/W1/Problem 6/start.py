# Pre-define the amount of hours, minutes and seconds are in a day
def_hours = 24
def_minutes = 1440
def_seconds = 86400

# Request an input from the user
input_days = int(input("Days: "))

# Calculate the hours, minutes and seconds
calc_hours = def_hours * input_days
calc_minutes = def_minutes * input_days
calc_seconds = def_seconds * input_days

# Print the result
print("Hours: " + str(calc_hours) + ", Minutes: " + str(calc_minutes) + ", Seconds: " + str(calc_seconds))
