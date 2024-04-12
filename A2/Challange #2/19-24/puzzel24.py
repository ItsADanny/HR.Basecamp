dict_24 = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 0, "l": 1, "m": 2, "n": 3, "o": 4, "p": 5, "q": 6, "r": 7, "s": 8, "t": 9, "u": 0, "v": 1, "w": 2, "x": 3, "y": 4, "z": 5}


def word_to_number(word):
    total_amount = ""

    for char in word:
        total_amount += str(dict_24[char.lower()])

    return total_amount


input_word = input("Enter an word: ")
print(word_to_number(input_word))