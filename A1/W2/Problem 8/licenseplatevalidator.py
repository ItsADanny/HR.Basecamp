__author__ = 'Danny de Snoo, HR-nr: 1091749'

# Request an input from the user
input_licenseplate = input("License: ")

# Split the input based on the "-"
splittedinput_licenseplate = input_licenseplate.split("-")

# Preform a simple check to see if the license plate includes 3 parts (Required for all license plates)
if len(splittedinput_licenseplate) < 0 or len(splittedinput_licenseplate) > 3:
    # If the license plate is an invalid length, print a invalid message.
    print("Invalid")
else:
    # If the license plate is a valid length, preform the rest of required checks

    # Split the 3 parts from the list into 3 variables
    license_p1 = splittedinput_licenseplate[0]
    license_p2 = splittedinput_licenseplate[1]
    license_p3 = splittedinput_licenseplate[2]

    # Preform the first check
    # ---------------------------------------------------------

    # ---------------------------------------------------------

    # Preform the second check
    # ---------------------------------------------------------

    # ---------------------------------------------------------

    # Preform the third check
    # ---------------------------------------------------------

    # ---------------------------------------------------------