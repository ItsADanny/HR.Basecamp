# NOTE:
# For a simple explanation on how to preform the binary to decimal conversion
# Use the following video: https://www.youtube.com/watch?v=VLflTjd3lWA

# Request an input from the user
input_binary = input("Binary: ")

# Predefine our output variable
output_decimal = 0

# First, reverse the input
reverse_input = input_binary[::-1]

# Define a variable which will store our current position
pos_num = 0
# Loop over the reversed input string
for i in reverse_input:
    # Preform a calculation of 2 to the power of our current position
    calc_number = 2 ** pos_num

    # Use the previously acquired number and times it with the number we currently have selected
    calc_total = calc_number * int(i)

    # Add it up to our total
    output_decimal += calc_total

    # Move the position
    pos_num += 1

# Finally, Output the result
print(output_decimal)
