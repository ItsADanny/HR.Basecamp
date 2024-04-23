import sys

try:
    file = open(sys.argv[1])
    lines = file.readlines()

    pos = 0
    lines_list = []
    for line in reversed(lines):
        if pos == 11:
            file.close()
            break
        if line != "":
            lines_list.append(line)
            pos += 1
    for line in reversed(lines_list):
        print(line.strip())

except IOError:
    print(f"Error reading file: {sys.argv[1]}")
except IndexError:
    print(f"Error reading file: {sys.argv[1]}")

if __name__ == "__main__":
    pass
