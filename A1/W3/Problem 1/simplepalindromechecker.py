# Request an input from the user
input_string = input("String: ")

# Reverse the string
reversed_string = input_string[::-1]

# Check if the result is the same as it's normally spelled
if reversed_string == input_string:
    print(f"\"{input_string}\" is a palindrome")
else:
    print(f"\"{input_string}\" is not a palindrome")