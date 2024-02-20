# This is a special version for codegrade, since it doens't allow the use of the [::1] shortcut

# Request an input from the user
input_string = input("String: ")

# Reverse the string
reversed_string = ""
for i in reversed(input_string):
    reversed_string += i

# Check if the result is the same as it's normally spelled
if reversed_string == input_string:
    print(f"\"{input_string}\" is a palindrome")
else:
    print(f"\"{input_string}\" is not a palindrome")