# Import the required module
import json
movies_data = None


# This function will import the movie's file into the program
def import_movies():
    movies_file = json.load(open('movies.json'))
    return movies_file


# This function will save the movie data from the program
# (This will also always be done when exiting the program)
def save_movies_data(movies):
    movies_file = open('movies.json', 'w')
    movies_file.write(json.dumps(movies))
    movies_file.close()


# This function will display all the available movie information
def movie_information():
    pass


# This function can be used to modify a movie's information
def movie_modify():
    pass


def movie_search(movie_title):
    # Here we will make a search function for searching movie titles
    pass


def movie_search_program(movie_title):
    # Here we will make a search function for searching movie titles
    # THIS VERSION IS SPECIFICALLY FOR THE PROGRAM AND NOT FOR IMPORT USAGE
    pass


def movie_change_title_or_release(movie_title, new_movie_title, new_movie_year):
    # Here we will make a change function that makes it possible to change a movies title
    # and or release date by searching for the movie's title
    pass


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
        movie_modify()
        return True
    elif choice == "s":
        while True:
            input_selected_movie = input("Enter movie title (or enter q to quit): ")
            if input_selected_movie.lower() == "q":
                print("Exiting function...")
                break
            else:
                movie_search(input_selected_movie)
                break
        return True
    elif choice == "c":
        while True:
            input_selected_movie = input("Enter movie title (or enter q to quit): ")
            if input_selected_movie.lower() == "q":
                print("Exiting function...")
                break
            else:
                is_available = movie_search_program(input_selected_movie)
                if is_available:
                    input_new_movie_title = input("Enter new movie title: ")
                    input_new_movie_year = input("Enter new movie year: ")
                    movie_change_title_or_release(input_new_movie_title, input_new_movie_title, input_new_movie_year)
                    break
                else:
                    print("Movie not found, please try again or exit out of this function")
        return True
    elif choice == "q":
        print("Quitting program, Thank you for using this program")
        save_movies_data(movies_data)
        return "Quit"
    else:
        print("Invalid, Please try again with a valid input")


if __name__ == "__main__":
    run_program()