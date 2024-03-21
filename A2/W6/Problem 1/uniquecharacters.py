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
    sets = {}

    for char in word:
        sets.add(char)

    unique = 0
    for set_value in sets:
        unique += 1

    return unique
