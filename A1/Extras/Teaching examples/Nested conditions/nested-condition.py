input_number = input("Enter your age: ")
input_name = input("Enter your name: ")

if input_number.isnumeric():
    if int(input_number) > 0:
        print(f"Hello {input_name}, you are {input_number} years of age")
    else:
        print(f"Hello {input_name}, you didn't fill in a valid number")
else:
    print(f"Hello {input_name}, you didn't fill in a number")