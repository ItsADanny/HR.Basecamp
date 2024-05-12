# Import the CSV function
import csv


def print_menu():
    print("[1] Print the amount of TV Shows")
    print("[2] Print the amount of Movies")
    print("[3] Print the (full) names of directors in alphabetical order who lead both tv shows and movies.\n"
          "(for example, search the name David Ayer. He is the director of three movies and one tv show)\n"
          "Treat multitple directors (seperated by comma) as 1 single director!")
    print("[4] Print the name of each director in alphabetical order,\n"
          "the number of movies and the number of tv shows (s)he was the director of.\n"
          "Use a tuple with format: (director name, number of movies, number of tv shows) to print.")


def load_csv_file(filename):
    # Open the extenal CSV file
    csvfile = open(filename)

    # Read the CSV file with the CSV Reader
    csvreader_csvfile = csv.reader(csvfile)

    # Create a list variable that will hold all the csv rows
    list_csv = []

    # preform a for-loop over the csvreader and store the csv rows in the list_studentcsv variable
    for row in csvreader_csvfile:
        list_csv.append(row)

    # Return all the data in the CSV file
    return list_csv


# This function returns the headers from the file content
def get_headers(file_content):
    headers = file_content[0]
    return headers


def search_by_type(file_content, show_type):
    pass


def search_by_director(file_content, director):
    pass


def get_directors(file_content):
    pass


def program():
    # print_menu()
    # print(load_csv_file("netflix_titles.csv"))
    # print(get_headers(load_csv_file("netflix_titles.csv")))


if __name__ == "__main__":
    program()
