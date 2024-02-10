__author__ = 'Danny de Snoo, HR-nr: 1091749'

# Define the variables required for calculation
def_months = 12
def_days = 365

# Request an input from the user
years = int(input("years: "))

# Calculate the amount of months and days are in the amount of years given by the user
calc_months = years * def_months
calc_days = years * def_days

# Print the result
print("Months: " + str(calc_months) + ", Days: " + str(calc_days))