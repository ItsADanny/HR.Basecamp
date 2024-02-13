__author__ = 'Danny de Snoo, HR-nr: 1091749'

# Request an input from the user
input_date = input("Please enter a date: ")

# First we remove all the white spaces
stripped_input_date = input_date.strip()

# Remove the "Month:", "Day:" and spaces that weren't removed by the strip function
stripped_input_date = stripped_input_date.replace("Month:", "")
stripped_input_date = stripped_input_date.replace("Day:", "")
stripped_input_date = stripped_input_date.replace(" ", "")

# Split the variables into a array
splitted_input_date = stripped_input_date.split(",")

# Seperate the array into 2 variables
int_month = splitted_input_date[0]
int_day = splitted_input_date[1]

# Preform the check to see which day it is
if int_month == "1" and int_day == "1":
    print("Nieuwjaarsdag")
elif int_month == "3" and int_day == "29":
    print("Goede Vrijdag")
elif int_month == "3" and int_day == "31" or int_month == "4" and int_day == "1":
    print("Pasen")
elif int_month == "4" and int_day == "27":
    print("Koningsdag")
elif int_month == "5" and int_day == "5":
    print("Bevrijdingsdag")
elif int_month == "5" and int_day == "9":
    print("Hemelvaartsdag")
elif int_month == "5" and int_day == "19" or int_month == "5" and int_day == "20":
    print("Pinksteren")
elif int_month == "12" and int_day == "5":
    print("Sinterklaas")
elif int_month == "12" and int_day == "25" or int_month == "12" and int_day == "26":
    print("Kerstmis")
else:
    print("No holiday found on given input")
