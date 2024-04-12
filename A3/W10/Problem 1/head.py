# Import the required modules
import random


# This function checks which input was given by the user,
# and then calls the corresponding function for the type of operation requested
def arithmetic_operation(input_operation):
    result = 0

    # Preform an if-elif-else check to see which input was given
    if input_operation.lower() == "summation":
        # If the requested operation was "summation",
        # then preform the "summation" function which gives back the result
        result = summation()
    elif input_operation.lower() == "multiplication":
        # If the requested operation was "multiplication",
        # then preform the "multiplication" function which gives back the result
        result = multiplication()
    elif input_operation.lower() == "subtraction":
        # If the requested operation was "subtraction",
        # then preform the "subtraction" function which gives back the result
        result = subtraction()
    else:
        # If the requested operation wasn't any of the possible operations,
        # then print an error message and set the result to 404 to not trigger the last print function
        print("Invalid operation given, Please run this application again and select a valid operation")
        result = 404

    if result != 404:
        # If the result isn't 404 then print this small string with your results
        print(f"You had {result} correct and {(10 - result)} incorrect answers in \"{input_operation}\"")

def summation():
    # Set the results to 0
    result = 0

    # Preform a for loop with a range of 10
    for i in range(10):
        # Generate 2 number between the 1 and 100
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        # Add both numbers up
        n_result = n1 + n2
        # Request a result for the given calculation
        input_awnser = input(f"{n1} + {n2} = ")
        # Check if it is the correct answer, if not do, nothing. If it is correct then add a 1 to the results
        if input_awnser.isnumeric() and input_awnser == n_result:
            result += 1

    # Return the results
    return result

def multiplication():
    # Set the results to 0
    result = 0

    # Preform a for loop with a range of 10
    for i in range(10):
        # Generate 2 number between the 1 and 100
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        # Add times both number
        n_result = n1 * n2
        # Request a result for the given calculation
        input_awnser = input(f"{n1} * {n2} = ")
        # Check if it is the correct answer, if not do, nothing. If it is correct then add a 1 to the results
        if input_awnser.isnumeric() and input_awnser == n_result:
            result += 1

    # Return the results
    return result


def subtraction():
    # Set the results to 0
    result = 0

    # Preform a for loop with a range of 10
    for i in range(10):
        # Generate 2 number between the 1 and 100
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        # Subtract both numbers
        n_result = n1 - n2
        # Request a result for the given calculation
        input_awnser = input(f"{n1} - {n2} = ")
        # Check if it is the correct answer, if not do, nothing. If it is correct then add a 1 to the results
        if input_awnser.isnumeric() and input_awnser == n_result:
            result += 1

    # Return the results
    return result


# Request an input from the user and then preform the function
input_operation = input("Arethmetic operation: ")
arithmetic_operation(input_operation)
