import sys

# Here we use a Try Except to see if the file does exist and if it can be read
try:
    # Open the file that has been given as an argument
    file = open(sys.argv[1])
    # Retriev the lines
    lines = file.readlines()

    # Set a position
    pos = 0
    # Create a list to store the lines
    lines_list = []
    # Loop through the lines
    for line in reversed(lines):
        # When we hit 10 lines printed, close the file and break out of the loop
        if pos == 11:
            file.close()
            break
        # Check if the line contains text, if not don't count it,
        # Else print it and count it as a valid line and update the pos
        if line != "":
            # Add the line to the list
            lines_list.append(line)
            # Update the position
            pos += 1
    # Now reverse print this line for the correct result
    for line in reversed(lines_list):
        print(line.strip())

# If the file can't be opened or read, we will print an error message that the file can't be opened/read
except IOError:
    print(f"Error reading file: {sys.argv[1]}")
except IndexError:
    print(f"Error reading file: {sys.argv[1]}")
