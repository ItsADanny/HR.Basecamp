import string

wordoccurence_dict = dict()
punctuation = string.punctuation

input_file = input("")

try:
    file = open(input_file, "r")
    lines = file.readlines()
    file.close()

    str_lines = ""
    for line in lines:
        for char in line:
            for punc in punctuation:
                if char == punc:
                    line = line.replace(punc, "")
        line = line.strip()
        str_lines += line

    splitted_words = str_lines.split(" ")

    for word in splitted_words:
        lowered_word = word.lower()
        if lowered_word not in wordoccurence_dict:
            wordoccurence_dict[lowered_word] = 1
        else:
            word_count = wordoccurence_dict[lowered_word]
            wordoccurence_dict[lowered_word] = (word_count + 1)

    most_wordoccurnences = 0
    most_wordoccurnences_word = ""
    for key, value in wordoccurence_dict.items():
        if value > most_wordoccurnences:
            most_wordoccurnences = value
            most_wordoccurnences_word = key

    least_wordoccurnences_list = []
    for key, value in wordoccurence_dict.items():
        if key != most_wordoccurnences_word:
            least_wordoccurnences_list.append(key)

    print(f"Most: ['{most_wordoccurnences_word}']")
    print(f"Least: {least_wordoccurnences_list}")
except FileNotFoundError:
    print(f"Error reading file: {input_file}")

if __name__ == "__main__":
    pass
