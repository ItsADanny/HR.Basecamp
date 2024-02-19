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
        # Create 3 variables to see if all parts are valid, to see on which part you currently are and what part each part is
        list_parts_type = []
        list_parts_char_num = []
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
                    list_parts_type += "a"
                elif i.isnumeric():
                    # Fully numeric, continue check
                    part += 1
                    list_parts_type += "n"
                else:
                    # If it's not fully an alphabetic or numeric part, Dean the part as invalid and continue check
                    invalid_parts += 1
                    part += 1

                list_parts_char_num.append(len(i))
            elif part == 1 and len(i) != 1:
                # If the second part is not 1 character long then continue the check, else dean it as an invalid part
                if i.isalpha():
                    part += 1
                    list_parts_type += "a"
                elif i.isnumeric():
                    part += 1
                    list_parts_type += "n"
                else:
                    invalid_parts += 1
                    part += 1

                list_parts_char_num.append(len(i))
            else:
                invalid_parts += 1
                part += 1

        # Check if there are any invalid parts detect.
        if invalid_parts == 0:
            check_isvalid = False

            print(f"list_parts_type: {list_parts_type}")
            print(f"list_parts_char_num: {list_parts_char_num}")

            if list_parts_type == ["a", "n", "n"] and list_parts_char_num == [2,2,2]:
                check_isvalid = True
            elif list_parts_type == ["n", "n", "a"] and list_parts_char_num == [2,2,2]:
                check_isvalid = True
            elif list_parts_type == ["n", "a", "n"] and list_parts_char_num == [2,2,2]:
                check_isvalid = True
            elif list_parts_type == ["a", "n", "a"] and list_parts_char_num == [2,2,2]:
                check_isvalid = True
            elif list_parts_type == ["a", "a", "n"] and list_parts_char_num == [2,2,2]:
                check_isvalid = True
            elif list_parts_type == ["n", "a", "a"] and list_parts_char_num == [2,2,2]:
                check_isvalid = True
            elif list_parts_type == ["n", "a", "n"] and list_parts_char_num == [2,3,1]:
                check_isvalid = True
            elif list_parts_type == ["n", "a", "n"] and list_parts_char_num == [1,3,2]:
                check_isvalid = True
            elif list_parts_type == ["a", "n", "a"] and list_parts_char_num == [2,3,1]:
                check_isvalid = True
            elif list_parts_type == ["a", "n", "a"] and list_parts_char_num == [1,3,2]:
                check_isvalid = True
            elif list_parts_type == ["a", "n", "a"] and list_parts_char_num == [3,2,1]:
                check_isvalid = True
            elif list_parts_type == ["n", "a", "n"] and list_parts_char_num == [1,2,3]:
                check_isvalid = True
            else:
                check_isvalid = False

            if check_isvalid:
                print("Valid")
            else:
                print("Invalid")
        else:
            # If there are print that its invalid
            print("Invalid")
else:
    print("Invalid")
