import sys

# Here we use a Try Except to see if the file does exist and if it can be read
try:
    # Open the file that has been given as an argument
    file = open(sys.argv[1])
    # Retriev the lines
    lines = file.readlines()

    # Set a position
    pos = 0
    # Loop through the lines
    for line in lines:
        # When we hit 10 lines printed, close the file and break out of the loop
        if pos == 11:
            file.close()
            break
        # Check if the line contains text, if not don't count it,
        # Else print it and count it as a valid line and update the pos
        if line != "":
            # Print a striped version of the line
            print(line.strip())
            # Update the position
            pos += 1
# If the file can't be opened or read, we will print an error message that the file can't be opened/read
except IOError:
    print(f"Error reading file: {sys.argv[1]}")
except IndexError:
    print(f"Error reading file: {sys.argv[1]}")

if __name__ == "__main__":
    pass
