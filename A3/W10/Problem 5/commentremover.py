# Request what the commented file's filename from the user
input_commentedfile = input("File to read: ")
# Request what the name will be for the cleaned file from the user
input_uncommentedfile = input("File to save: ")

# Preform a check to see if the uncommented ("Cleand") file ends with .txt
if input_uncommentedfile.endswith(".txt"):
    # Use try/Except to see if you can open the file and preform the required functions
    try:
        # Open the file in READ MODE
        original_file = open(input_commentedfile, "r")
        # Retrieve the file's content
        file_content = original_file.read()
        # Close the file
        original_file.close()

        # Create a new file and open it with WRITE MODE
        cleaned_file = open(input_uncommentedfile, "w")

        # Loop through the lines
        for line in file_content.split("\n"):
            # If the line starts with a # ignore it
            if line.startswith("#"):
                pass
            # If it doesn't start with a # then add it to the cleaned file
            else:
                cleaned_file.write(line)
                cleaned_file.write("\n")

        # Close the cleaned file
        cleaned_file.close()

    except FileNotFoundError:
        # If there is any problem, then print that there is an error with reading the file
        print(f"Error reading file: {input_commentedfile}")
else:
    # If the Cleaned file name is invalid, print an error message
    print(f"Invalid cleaned file name. File must end with \".txt\"")
