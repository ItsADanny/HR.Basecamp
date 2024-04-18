# Request what the commented file's filename from the user
input_commentedfile = input("File to read: ")


# Use try/Except to see if you can open the file and preform the required functions
try:
    # Open the file in READ MODE
    original_file = open(input_commentedfile, "r")
    # Retrieve the file's content
    file_content = original_file.read()
    # Close the file
    original_file.close()

    # Create a variable that will hold our current line position
    pos_line = 1
    # Create a variable that will hold the previous line for comparison later
    prev_line = ""
    # Loop through the lines
    for line in file_content.split("\n"):
        # If the line starts with a # ignore it
        if line.startswith("def "):
            # Check if the previous line started with a # to see if there was a comment
            if prev_line.startswith("#"):
                # If there was a comment, then ignore this function
                pass
            else:
                # If there wasn't a comment in the previous line, Retriev the function name, and print a message

                # Strip and replace parts of the line so that we only have the function
                function_name = line.strip()
                function_name = function_name.replace(":", "")
                function_name = function_name.replace("def ", "")

                # Print the message
                print(f"File: {input_commentedfile} contains a function [{function_name}] on line [{pos_line}] "
                      f"without a preceding comment.")

        # Move the pos line to the next line and set the prev_line to the line that we just read
        pos_line += 1
        prev_line = line

except FileNotFoundError:
    # If there is any problem, then print that there is an error with reading the file
    print(f"Error reading file: {input_commentedfile}")
