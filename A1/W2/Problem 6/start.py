# pre-define the response variable
def_response = ""

# Request an input from the user
input_years = float(input("Human years: "))

if input_years < 0:
    def_response = "Only positive numbers are allowed"
else:
    # Define the calculation variable
    calc_dogyears = 0

    if input_years < 3:
        calc_dogyears = input_years * 10.5
    else:
        input_years = input_years - 2
        calc_dogyears = (input_years * 4) + 21

    # Complete the response we are going to send back
    def_response = "Dog years: " + str(calc_dogyears)

print(def_response)
