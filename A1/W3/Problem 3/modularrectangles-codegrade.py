# Request a Width from the user
input_width = input("")
# Request a height from the user
input_height = input("")

check_numeric_input = False

# prefrom a check to see if the width and height are a number
if input_width.isnumeric() and input_height.isnumeric():
    check_numeric_input = True

# If both inputs are numeric continue the program
if check_numeric_input:
    curr_row = 0
    curr_num = 0
    # Preform a while loop with the following condition: if curr_row is not equal to the input height preform the loop
    while curr_row != int(input_height):
        curr_pos = 0
        str_row = ""
        # Preform a while loop with the following condition: if curr_pos is not equal to the input width preform the loop
        while curr_pos != int(input_width):
            if curr_num >= 10:
                curr_num = 0

            # Check if it's the first character in the row, if so don't add a space, else add a space
            if str_row == "":
                str_row += str(curr_num)
            # THIS IS REQUIRED FOR CODEGRADES AUTO DETECT FEATURE
            elif curr_pos == (int(input_width) - 1):
                str_row += " "+str(curr_num)+" "
            else:
                str_row += " "+str(curr_num)

            curr_pos += 1
            curr_num += 1

        # When to row is done, print the row and continue the program until the desired result has been reached
        curr_row += 1
        print(str_row)
# If one or both of the inputs aren't numeric present the user with an error message
else:
    print("Error: Incorrect input. Please enter a valid input width and height.")
