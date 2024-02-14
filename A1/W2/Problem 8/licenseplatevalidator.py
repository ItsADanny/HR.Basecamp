__author__ = 'Danny de Snoo, HR-nr: 1091749'

# Request an input from the user
input_licenseplate = input("License: ")

# Preform a first check to see if the license plate is a valid length
if len(input_licenseplate) == 8:
    # Split the input based on the "-"
    splittedinput_licenseplate = input_licenseplate.split("-")

    # Preform a simple check to see if the license plate includes 3 parts (Required for all license plates)
    if len(splittedinput_licenseplate) < 0 or len(splittedinput_licenseplate) > 3:
        # If the license plate is an invalid length, print an invalid message.
        print("Invalid")
    else:
        # Create 2 variables to see if all parts are valid and to see on which part you currently are
        invalid_parts = 0
        part = 0

        # do a for-loop over the license plate parts
        for i in splittedinput_licenseplate:
            if len(i) <= 3 and part != 1:
                # If the license plate part is a valid length and not the second part then continue the check.
                # Check if it's a full alphabetic part or a full numeric part
                if i.isalpha():
                    # Fully alphabetic, continue check
                    part += 1
                elif i.isnumeric():
                    # Fully numeric, continue check
                    part += 1
                else:
                    # If it's not fully an alphabetic or numeric part, Dean the part as invalid and continue check
                    invalid_parts += 1
                    part += 1
            elif part == 1 and len(i) != 1:
                # If the second part is not 1 character long then continue the check, else dean it as an invalid part
                if i.isalpha():
                    part += 1
                elif i.isnumeric():
                    part += 1
                else:
                    invalid_parts += 1
                    part += 1
            else:
                invalid_parts += 1
                part += 1

        # Check if there are any invalid parts detect.
        if invalid_parts == 0:
            # If not print that its valid
            print("Valid")
        else:
            # If there are print that its invalid
            print("Invalid")
else:
    print("Invalid")
