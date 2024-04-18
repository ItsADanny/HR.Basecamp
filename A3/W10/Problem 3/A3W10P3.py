input_file = input("")

try:
    # Open the file (In READ MODE)
    file = open(input_file, "r")
    # Retrieve all the lines in the file
    lines = file.readlines()
    # Close the file
    file.close()

    # Loop through the lines, Strip all the white spaces and add them to a giant string variable
    str_filelines = ""
    for line in lines:
        # Only add stripped versions of the lines (That also had the \n removed!)
        striped_line = line.strip()
        striped_flat_line = striped_line.replace("\n", "")

        # Add the line to the giant string variable
        str_filelines += striped_flat_line

    # Split the giant string into a list
    list_str_filelines = str_filelines.split()

    smallest_word_len = 100
    smallest_word = ""
    largest_word_len = 0
    largest_word = ""
    for word in list_str_filelines:
        if len(word) > largest_word_len:
            largest_word_len = len(word)
            largest_word = word
        if len(word) < smallest_word_len:
            smallest_word_len = len(word)
            smallest_word = word

    average_len = largest_word_len - smallest_word_len

    print(smallest_word_len)
    print(smallest_word)
    print(largest_word_len)
    print(largest_word)
    print(average_len)

except FileNotFoundError:
    print("File")


