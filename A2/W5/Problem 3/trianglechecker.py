# Predefine the following variables for the while-loop that will be used for the user's response validation
input_straw_list = []
sides = ["A", "B", "C"]
pos = 0


# This function checks all sides of the given sides with each other to see
def check_triangle(side_a, side_b, side_c):
    # Make a list of all the sides
    list = [side_a, side_b, side_c]
    # Pre-define a valid_checks variable with an initial number of 3,
    # if at the end of the function this the number is still 3 then it's possible
    # to make a triangle with these numbers
    valid_checks = 3

    # Preform a for loop with a range of 3
    for i in range(3):

        # Get the first side
        side1_check = list[i]
        # Get the position of the next sides
        pos2_check = i + 1
        pos3_check = i + 2

        # Preform a check to see if the numbers you calculated above arent
        # above a certain number that would cause an out-of-range issue
        if pos2_check == 3:
            pos2_check = 0

        if pos3_check >= 3:
            if i == 2:
                pos3_check = 1
            else:
                pos3_check = 0

        # Check if it's possible to make a triangle, if not then do a -1 on the valid_checks
        if side1_check >= (list[pos2_check] + list[pos3_check]):
            valid_checks -= 1

    # If the number is still 3 after all the checks, then return a True else return a False
    if valid_checks == 3:
        return True
    else:
        return False


# Preform a while loop that only stops when 3 items have been inputted and have been stored into the list
while len(input_straw_list) != 3:
    # Set the response to 0 and the valid_response to False
    user_response = 0
    valid_response = False
    # While to response is not valid preform this loop
    while not valid_response:
        # Request a number from the user for a certain side
        input_straw = input(f"Side {sides[pos]}: ")
        # Check if the number is numeric, If not give an error message, else turn the input into a string,
        # set user_response to this number and turn valid_response to True
        if input_straw.isnumeric():
            user_response = int(input_straw)
            valid_response = True
        else:
            print(f"Invalid input, please enter a valid number for side {sides[pos]}")
    # Add the number to the list
    input_straw_list += [user_response]
    # Move the position
    pos += 1

# Preform the function in an if-else statement and print if its possible triangle
# , or an impossible triangle after getting the results from the function
if check_triangle(input_straw_list[0], input_straw_list[1], input_straw_list[2]):
    print("Possible triangle")
else:
    print("Impossible triangle")