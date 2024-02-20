# Predefine a list with all the available punctuations
def_punctuations = '''!()-[]{};*:'",<>./?@_~'''

# Request an input from the user
input_string = input("String: ")

stripped_string = input_string.strip()
# Loop over the string and punctuation list to see if there are any punctuations used, and if so replace them
for i in stripped_string:
    if i in def_punctuations:
        stripped_string = stripped_string.replace(i, "")

# Make all the characters lowercase
stripped_string = stripped_string.lower()

# Reverse the string
reversed_string = stripped_string[::-1]

# Check if the result is the same as it's normally spelled
if reversed_string == stripped_string:
    print(f"\"{input_string}\" is a palindrome")
else:
    print(f"\"{input_string}\" is not a palindrome")