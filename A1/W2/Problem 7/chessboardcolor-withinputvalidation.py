__author__ = 'Danny de Snoo, HR-nr: 1091749'

# Define a list of valid Letter positions
def_chessboard_letter_pos = ["a", "b", "c", "d", "e", "f", "g", "h"]

# request an input from the user
input_chessposition = input("Position: ")

# Check if the position given is a valid length
if len(input_chessposition) >= 3:
    print("Invalid length, Please provide an valid position")
else:
    # Retrieve the first and second part from the position
    input_pos_p1 = input_chessposition[0]
    input_pos_p2 = input_chessposition[1]

    p2_validnumber = False

    # validate that number has been given in the position
    try:
        int_p2 = int(input_pos_p2)
        if int_p2 < 9:
            # If the number given is below a 9 then it is good to go
            p2_validnumber = True
        else:
            print("Invalid position given, Please provide an valid position")
    except ValueError:
        print("Invalid position given, Please provide an valid position")

    # if the position passes the number validation then validate the letter position
    if p2_validnumber:
        p1_validletter = False

        # Check if the character is an Alphabetic character
        if input_pos_p1.isalpha():
            temp_letter = input_pos_p1.lower()

            # Check if the character that has been inputted by the user is valid for in a
            # chessboard following the definition we provided in the definition above
            if any(x in temp_letter for x in def_chessboard_letter_pos):
                p1_validletter = True
            else:
                print("Invalid position given, Please provide an valid position")
        else:
            print("Invalid position given, Please provide an valid position")

        if p1_validletter:
            # Define the starting positions
            selected_letter_pos_int = 0
            next_pos = 0

            # Loop over the chessboard letter position definition we made and if i match has been found then save that
            # number to which the letter position is linked
            for i in def_chessboard_letter_pos:
                if input_pos_p1.lower() == i:
                    selected_letter_pos_int = next_pos
                else:
                    next_pos = next_pos + 1

            # After getting the letter position translated into a number, preform a modular arithmetic calculation
            # and output the color of the position
            if selected_letter_pos_int % int(input_pos_p2):
                print("White")
            else:
                print("Black")
