# Request an input from the user
input_string = input("String: ")

# Remove the whitespaces in the string
stripped_string = input_string.strip()
cleaned_string = stripped_string.replace(" ", "")

# Reverse the string
reversed_string = cleaned_string[::-1]

# Check if the result is the same as it's normally spelled
if reversed_string == cleaned_string:
    print(f"\"{input_string}\" is a palindrome")
else:
    print(f"\"{input_string}\" is not a palindrome")
