# Pre-define the tax rates that are going to be used in the calculations
def_taxpercentage = 0.21
def_tippercentage = 0.15

# Request input from the user
input_cost = float(input("Cost of the meal: "))

# Calculate the amount of tax, the tip and the total of your order
calc_tax = round((float(input_cost) * def_taxpercentage), 3)
calc_tip = round((float(input_cost) * def_tippercentage), 3)
calc_total = round((calc_tax + calc_tip + input_cost), 3)

# Print the result
print("Tax: " + str(calc_tax) + " , Tip: " + str(calc_tip) + " , Total: " + str(calc_total))
