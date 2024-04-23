def movie_search():
    # Here we will make a search function for searching movie titles


def movie_change_title_or_release():
    # Here we will make a change function that makes it possible to change a movies title
    # and or release date by searching for the movies title


# In this function, we will print the program's menu
def print_menu():
    print("[I] Movie information overview")
    print("[M] Make modification based on assignment")
    print("[S] Search a movie title")
    print("[C] Change title and/or release year by search on title")
    print("[Q] Quit program")


# In this function, we will make the program run
def run_program():
    # This will keep the program running until the user quits the program
    while True:
        # Print the UI
        print_menu()
        # Request an input from the user
        choice = input("")
        # When you receive an input from the user, send the choice (with lower preformed on it)
        return_value = program_function(choice.lower())

        # When the return value equals "Quit" then exit the loop and end the program
        if return_value == "Quit":
            break


# This function will compare the "choice" that the user has inputted and will run the associated function
def program_function(choice):
    if choice == "i":

        return True
    elif choice == "m":

        return True
    elif choice == "s":
        movie_search()
        return True
    elif choice == "c":
        movie_change_title_or_release()
        return True
    elif choice == "q":
        print("Quitting program, Thank you for using this program")
        return "Quit"
    else:
        print("Invalid, Please try again with a valid input")


if __name__ == "__main__":
    run_program()