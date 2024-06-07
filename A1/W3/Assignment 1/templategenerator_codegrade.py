# Predefined application variables
min_salary = 20000.00
max_salary = 80000.00
valid_years = [2021, 2022]


# This function is used to gather the necessary data for a Job offer letter
def create_joboffer():
    return_data_list = list()
    while True:
        input_firstname = input("First Name? ")
        if check_name(input_firstname):
            return_data_list.append(input_firstname)
            break
        else:
            print("Input error")
    while True:
        input_lastname = input("Last Name? ")
        if check_name(input_lastname):
            return_data_list.append(input_lastname)
            break
        else:
            print("Input error")
    while True:
        input_title = input("Title? ")
        if check_jobtitle(input_title):
            return_data_list.append(input_title)
            break
        else:
            print("Input error")
    while True:
        input_salary = input("Annual Salary? ")
        if isfloat(input_salary.replace(".", "").replace(",", ".")):
            if check_salary(float(input_salary.replace(".", "").replace(",", "."))):
                return_data_list.append(input_salary)
                break
            else:
                print("Input error")
        else:
            print("Input error")
    while True:
        input_startdate = input("Start Date?(YYYY-MM-DD) ")
        if isdateformat(input_startdate):
            if check_startdate(input_startdate):
                return_data_list.append(input_startdate)
                break
            else:
                print("Input error")

    # Return the required data
    return return_data_list


# This function is used to gather the necessary data for a Rejection letter
def create_rejection():
    return_data_list = list()
    while True:
        input_firstname = input("First Name? ")
        if check_name(input_firstname):
            return_data_list.append(input_firstname)
            break
        else:
            print("Input error")
    while True:
        input_lastname = input("Last Name? ")
        if check_name(input_lastname):
            return_data_list.append(input_lastname)
            break
        else:
            print("Input error")
    while True:
        input_title = input("Title? ")
        if check_jobtitle(input_title):
            return_data_list.append(input_title)
            break
        else:
            print("Input error")
    while True:
        input_dofeedback = input("Feedback? (Yes or No) ").lower()
        if input_dofeedback == "yes":
            input_feedback = input("Enter your Feedback (One Statement): ")
            return_data_list.append(input_feedback)
        elif input_dofeedback == "no":
            return_data_list.append("")
            break
        else:
            print("Input error")

    # Return the required data
    return return_data_list


# This function will compile the final letter for a job offer
def compile_joboffer(letter_data: list) -> list:
    result = [f"Dear {letter_data[0]} {letter_data[1]},",
              f"After careful evaluation of your application for the position of {letter_data[2]},",
              f"we are glad to offer you the job. Your salary will be {letter_data[3]} euro annually.",
              f"Your start date will be on {letter_data[4]}. "
              f"Please do not hesitate to contact us with any questions.", "Sincerely,", "HR Department of XYZ"]
    return result


# This function will compile the final letter for a rejection letter
def compile_rejection(letter_data: list) -> list:
    result = [f"Dear {letter_data[0]} {letter_data[1]},",
              f"After careful evaluation of your application for the position of {letter_data[2]},",
              "at this moment we have decided to proceed with another candidate."]
    # Check to see if there is any feedback, if so add that part, else don't add anything
    if letter_data[3] != "":
        result.append("Here we would like to provide you our feedback about the interview.")
        result.append(f"{letter_data[3]}")

    result.append("Sincerely,")
    result.append("HR Department of XYZ")
    return result


def check_name(name: str) -> bool:
    if 2 < len(name) <= 10 and name[0] == name[0].upper() and name.replace(" ", "").isalpha():
        return True
    return False


def check_jobtitle(title: str) -> bool:
    if len(title) >= 10 and title.replace(" ", "").isalpha():
        return True
    return False


def check_salary(salary: float) -> bool:
    if 20000.0 < salary < 80000.0:
        return True
    return False


def check_startdate(startdate: str) -> bool:
    list_split_date = startdate.split("-")
    if len(list_split_date[0]) == 4 and len(list_split_date[1]) == 2 and len(list_split_date[2]) == 2:
        if list_split_date[0].isdigit() and list_split_date[1].isdigit() and list_split_date[2].isdigit():
            if (int(list_split_date[0]) in valid_years and 1 <= int(list_split_date[1]) <= 12
                    and 1 <= int(list_split_date[2]) <= 31):
                return True
    return False


def isdateformat(value: str) -> bool:
    if value[4] == "-" and value[7] == "-":
        return True
    return False


def isfloat(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


# This function is used to display the compiled letters
def display(letter: list):
    print("Here is the final letter to send:")
    for row in letter:
        print(row)


def main():
    first_time = True
    while True:
        if first_time:
            input_choice = input("Do you want to make a letter? (Yes or No): ").lower()
        else:
            input_choice = input("More Letters? (Yes or No): ")
        if input_choice == "yes":
            while True:
                input_lettertype = input("Job Offer or Rejection?: ").lower()
                if input_lettertype == "job offer":
                    list_joboffer_data = create_joboffer()
                    joboffer = compile_joboffer(list_joboffer_data)
                    display(joboffer)
                    break
                elif input_lettertype == "rejection":
                    list_rejection_data = create_rejection()
                    rejection = compile_rejection(list_rejection_data)
                    display(rejection)
                    break
                else:
                    print("Input error")
        elif input_choice == "no":
            break
        else:
            print("Input error")


if __name__ == '__main__':
    main()
