# Use a list of dictionaries for datastorage with the following attribute fields: [title, author, publisher, pub_date]

# Define a boolean that will be True unless the user quits the program
running = True
# Define a list that will store our dictionaries
book_storage = []


# This function is for adding a book
def add_book(book):
    splitted_input = book.split(",")
    book_title = splitted_input[0]
    book_author = splitted_input[1]
    book_publisher = splitted_input[2]
    book_year = splitted_input[3]

    book_dict = {'title': book_title, 'author': book_author, 'publisher': book_publisher, 'pub_date': book_year}
    book_storage += book_dict
    print(f"book_dict : {book_dict}")
    print(f"book_storage : {book_storage}")

# This function is to search for a book
def search_book(books, term):
    book_found = False
    for book in book_storage:
        book_title = str(book['title'])
        book_author = book['author']
        book_publisher = book['publisher']

        if book_title.find(term) or book_author.find(term) or book_publisher.find(term):
            book_found = True

    return book_found


# This function is for exiting
def exit_program():
    for book in book_storage:
        print(book)

while running:
    print("[A] Add book")
    print("[S] Search book")
    print("[E] Exit (and print)")
    input_option = input("What option would you like to select : ")
    if input_option == "A":
        input_book = input("Book details: ")

    elif input_option == "S":
        input_book = input("Search term: ")
    elif input_option == "E":
        running = False
        exit_program()
    else:
        print("Invalid input, Please select an valid option : ")
