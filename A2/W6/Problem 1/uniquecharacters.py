def unique_chars_dict(word):
    dicts = dict()

    for char in word:
        if char not in dicts:
            dicts[char] = char

    unique = 0
    for dictionary_value in dicts.values():
        unique += 1

    return unique


def unique_chars_set(word):
    sets = set()

    for char in word:
        sets.add(char)

    unique = 0
    for set_value in sets:
        unique += 1

    return unique


if __name__ == "__main__":
    input_word = input("What word would you like to use?")
    print(unique_chars_dict(input_word))
    print(unique_chars_set(input_word))
