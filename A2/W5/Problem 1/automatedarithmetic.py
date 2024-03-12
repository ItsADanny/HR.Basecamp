# Import the required modules
import random

def arithmetic_operation(input_operation):
    result = 0

    if input_operation.lower() == "summation":
        result = summation()
    elif input_operation.lower() == "multiplication":
        result = multiplication()
    elif input_operation.lower() == "subtraction":
        result = subtraction()
    else:
        print("Invalid operation given, Please run this application again and select a valid operation")
        result = 404

    if result != 404:
        print(f"You had {result} correct and {(10 - result)} incorrect answers in \"{input_operation}\"")

def summation():
    result = 0

    for i in range(10):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        n_result = n1 + n2
        input_awnser = input(f"{n1} + {n2} = ")
        if input_awnser.isnumeric() and input_awnser == n_result:
            result += 1

    return result

def multiplication():
    result = 0

    for i in range(10):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        n_result = n1 * n2
        input_awnser = input(f"{n1} * {n2} = ")
        if input_awnser.isnumeric() and input_awnser == n_result:
            result += 1

    return result


def subtraction():
    result = 0

    for i in range(10):
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        n_result = n1 - n2
        input_awnser = input(f"{n1} - {n2} = ")
        if input_awnser.isnumeric() and input_awnser == n_result:
            result += 1

    return result


input_operation = input("Arethmetic operation: ")
arithmetic_operation(input_operation)
