# Define a boolean that will keep the program running until the user wishes to exit the program
bool_program_done = False


# This is a function that generates a
def triangle_generator():
    global bool_program_done

    # Request an input from the user
    input_triangle = input("How large would you like the triangle to be? (Type: N, to exit the program) : ")

    invalid_input = False
    if input_triangle.isnumeric():
        input_triangle_integer = int(input_triangle)
        triangle = []
        next_point_amount = input_triangle_integer
        while range(input_triangle_integer) != len(triangle):
            triangle_row = ""
            points = 0
            while points != input_triangle_integer:
                if triangle_row == "":
                    triangle_row = "*"
                else:
                    triangle_row += " *"
                points += 1
            triangle += [triangle_row]

            print(f"range(input_triangle_integer) = {input_triangle_integer}")
            print(f"len(triangle) = {len(triangle)}")
            print(triangle_row)

        pos = 0
        while range(len(triangle)):
            print(triangle[pos])

            pos += 1

    elif input_triangle.isalpha():
        if input_triangle.lower() == "n":
            print("Shutting down the program...")
            print("Thank you for using this program")
            print("-Danny")
            bool_program_done = True
        else:
            invalid_input = True
    else:
        invalid_input = True

    if invalid_input:
        print("Invalid input, please try a valid number")


while not bool_program_done:
    triangle_generator()
