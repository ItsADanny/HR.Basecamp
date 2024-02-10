# Define a variable that will function as a global variable to stop the program
glob_var_done = False

# Define a function for making a letter
def lettergenerator():
    global glob_var_done
    input_moreletters = input("More Letters?(Yes or No): ")

    if input_moreletters == "No":
        glob_var_done = True
    else:
        input_lettertype = input("Job Offer or Rejection?: ")

        if input_lettertype == "" or input_lettertype == "":

while glob_var_done == False:
    lettergenerator()

# TODO finish this assignment: Information can be found in Codegrade.