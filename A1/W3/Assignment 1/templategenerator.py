# Define a variable that will function as a global variable to stop the program
glob_var_done = False
FirstTime = True

def template_generator():
    # Retrieve the global variable to shut down the program
    global glob_var_done

    if FirstTime:
        user_input = input("Do you want to make a letter? (Yes or No): ")
    else:
        user_input = input("More Letters? (Yes or No): ")

    if user_input == "Yes":

        # Retrieve the Letter type
        valid_lettertype = False
        lettertype = 0
        while not valid_lettertype:
            input_lettertype = input("Job Offer or Rejection?: ")
            if input_lettertype == "Job Offer":
                lettertype = 1
                valid_lettertype = True
            elif input_lettertype == "Rejection":
                lettertype = 2
                valid_lettertype = True
            else:
                print("Invalid Lettertype, Please use a valid lettertype")

        # Retrieve the First name (And check if it's valid)
        valid_frst_name = False
        firstname = ""
        while not valid_frst_name:
            input_firstname = input("First Name?: ")

            if 2 < len(input_firstname) <= 10:
                result_isalpha = input_firstname.isalpha()
                result_isfirstupper = False
                if input_firstname[0] == input_firstname[0].upper():
                    result_isfirstupper = True
                if result_isalpha and result_isfirstupper:
                    firstname = input_firstname
                    valid_frst_name = True
                else:
                    print("Invalid first name, Please use a valid first name")
            else:
                print("Invalid first name, Please use a valid first name")

        # Retrieve the Last name (And Check if it's valid)
        valid_last_name = False
        lastname = ""
        while not valid_last_name:
            input_lastname = input("Last Name?: ")

            if 2 < len(input_lastname) <= 10:
                result_isalpha = input_lastname.isalpha()
                result_isfirstupper = False
                if input_lastname[0] == input_lastname[0].upper():

                    result_isfirstupper = True
                if result_isalpha and result_isfirstupper:
                    lastname = input_lastname
                    valid_last_name = True
                else:
                    print("Invalid last name, Please use a valid last name")
            else:
                print("Invalid last name, Please use a valid last name")

        valid_job_title = False
        job_title = ""
        while not valid_job_title:
            input_jobtitle = input("Job Title?: ")

            temp_input_jobtitle = input_jobtitle.strip()
            temp_input_jobtitle = temp_input_jobtitle.replace(" ", "")
            result_isalpha = temp_input_jobtitle.isalpha()
            result_isgoodlength = False
            if len(input_jobtitle) >= 10:
                result_isgoodlength = True

            if result_isalpha and result_isgoodlength:
                job_title = input_jobtitle
                valid_job_title = True

            print(f"result_isalpha: {result_isalpha}")
            print(f"result_isgoodlength: {result_isgoodlength}")

        if lettertype == 1:
            # Job Offer
            valid_salary = False
            salary = float(0)
            while not valid_salary:
                input_salary = input("Annual Salary?: ")

                isfloat = False
                try:
                    temp_input_salary = input_salary.replace(".", "")
                    temp_input_salary = temp_input_salary.replace(",", ".")
                    print(f"temp_input_salary {temp_input_salary}")
                    temp_float_test = float(temp_input_salary)
                    isfloat = True
                except ValueError:
                    print("Invalid salary given, Give a valid salary (example: 20.000,00)")

                if isfloat:
                    temp_input_salary = input_salary.replace(".", "")
                    temp_input_salary = temp_input_salary.replace(",", ".")
                    float_input_salary = float(temp_input_salary)
                    if 20000 < float_input_salary < 80000:
                        salary = input_salary
                        valid_salary = True
                    else:
                        print("Invalid salary given, Give a valid salary (salary must be between 20.000,00 and 80.000,00)")

            valid_startdate = False
            startdate = ""
            while not valid_startdate:
                input_startdate = input("Start Date?(YYYY-MM-DD) : ")

                input_year = input_startdate[0:4]
                input_month = input_startdate[5:7]
                input_day = input_startdate[8:10]

                valid_date = False
                if input_year in ["2020", "2021"]:
                    if input_month.isnumeric():
                        int_input_month = int(input_month)
                        if 0 < int_input_month < 13:
                            if input_day.isnumeric():
                                int_input_day = int(input_day)
                                if 0 < int_input_day < 31:
                                    startdate = input_startdate
                                    valid_date = True
                                    valid_startdate = True

                if not valid_date:
                    print("Invalid date, Please input a valid date (YYYY-MM-DD)")

            generate_joboffer(firstname, lastname, job_title, salary, startdate)

        elif lettertype == 2:
            # Rejection Letter
            feedback = False
            valid_feedback_response = False
            while not valid_feedback_response:
                input_feedback = input("Feedback? (Yes or No): ")

                if input_feedback.isalpha():
                    if input_feedback.upper() == "YES":
                        feedback = True
                        valid_feedback_response = True
                    elif input_feedback.upper() == "NO":
                        feedback = False
                        valid_feedback_response = True
                    else:
                        print("Invalid")
                else:
                    print("Invalid")

            feedback_str = ""
            if feedback:
                input_feedback = input("Enter your Feedback (One Statement): ")
                feedback_str = input_feedback

            generate_rejection(firstname, lastname, job_title, feedback_str)
        else:
            print("Invalid Lettertype, Please use a valid lettertype")
    else:
        glob_var_done = True

def generate_joboffer(frst_name, last_name, job_title, annu_slry, strt_date):
    result = []
    result += f"Dear {frst_name} {last_name}"
    result += f"After careful evaluation of your application for the position of {job_title},"
    result += f"we are glad to offer you the job. Your salary will be {annu_slry} euro annually."
    result += f"Your start date will be on {strt_date}. Please do not hesitate to contact us with any questions."
    result += "Sincerely,"
    result += "HR Department of XYZ"
    return result

def generate_rejection(frst_name, last_name, job_title, feedback):
    result = []
    result += f"Dear {frst_name} {last_name}"
    result += f"After careful evaluation of your application for the position of {job_title},"
    result += "at this moment we have decided to proceed with another candidate."
    #Check to see if there is any feedback, if so add that part, else don't add anything
    if feedback != "":
        result += "Here we would like to provide you our feedback about the interview."
        result += f"{feedback}"

    result += "Sincerely,"
    result += "HR Department of XYZ"
    return result


while not glob_var_done:
    template_generator()
