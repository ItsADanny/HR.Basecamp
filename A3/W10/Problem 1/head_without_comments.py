import sys

try:
    file = open(sys.argv[1])
    lines = file.readlines()

    pos = 0
    for line in lines:
        if pos == 11:
            file.close()
            break
        if line != "":
            print(line.strip())
            pos += 1

except IOError:
    print(f"Error reading file: {sys.argv[1]}")
except IndexError:
    print(f"Error reading file: {sys.argv[1]}")