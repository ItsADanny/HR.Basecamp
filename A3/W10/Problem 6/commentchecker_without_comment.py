input_commentedfile = input("File to read: ")

try:
    original_file = open(input_commentedfile, "r")
    file_content = original_file.read()
    original_file.close()

    pos_line = 1
    prev_line = ""
    for line in file_content.split("\n"):
        if line.startswith("def "):
            if prev_line.startswith("#"):
                pass
            else:
                function_name = line.strip()
                function_name = function_name.replace(":", "")
                function_name = function_name.replace("def ", "")

                print(f"File: {input_commentedfile} contains a function [{function_name}] on line [{pos_line}] "
                      f"without a preceding comment.")

        pos_line += 1
        prev_line = line

except FileNotFoundError:
    print(f"Error reading file: {input_commentedfile}")

if __name__ == "__main__":
    pass
