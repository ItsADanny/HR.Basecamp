input_commentedfile = input("File to read: ")
input_uncommentedfile = input("File to save: ")

if input_uncommentedfile.endswith(".txt"):
    try:
        original_file = open(input_commentedfile, "r")
        file_content = original_file.read()
        original_file.close()

        cleaned_file = open(input_uncommentedfile, "w")

        for line in file_content.split("\n"):
            if line.startswith("#"):
                pass
            else:
                cleaned_file.write(line)
                cleaned_file.write("\n")

        cleaned_file.close()

    except FileNotFoundError:
        print(f"Error reading file: {input_commentedfile}")
else:
    print(f"Invalid cleaned file name. File must end with \".txt\"")

if __name__ == "__main__":
    pass
