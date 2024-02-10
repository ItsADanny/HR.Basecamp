__author__ = 'Danny de Snoo, HR-nr: 1091749'

# request an input from the user
input_numbers = input()

# Create a string and an int in which we are going to use to process and later display the results from the input
string_numbers = ""
calc_finalresult = 0

# for-Loop over the input so that you can split the number easily from the input
for i in input_numbers:
    # Check if the text string_numbers is empty,
    # if so just add the number to the string, else add a + and the number onto the string
    if not string_numbers:
        string_numbers += i
    else:
        string_numbers += "+" + i
    # Add the number up into our calc_finalresult variable which is stored outside the for-loop
    calc_finalresult = calc_finalresult + int(i)

# print the final result
print(f"{string_numbers}={calc_finalresult}")
