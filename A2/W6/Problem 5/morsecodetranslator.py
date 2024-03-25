to_morse_code_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
                      "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.",
                      "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "w": ".--", "v": "...-", "x": "-..-",
                      "y": "-.--", "z": "--..", ",": "--..--", ".": ".-.-.-", "?": "..--..", "!": "-.-.--"}
from_morse_code_dict = {".-": "a", "-...": "b", "-.-.": "c", "-..": "d", ".": "e", "..-.": "f", "--.": "g", "....": "h",
                        "..": "i", ".---": "j", "-.-": "k", ".-..": "l", "--": "m", "-.": "n", "---": "o", ".--.": "p",
                        "--.-": "q", ".-.": "r", "...": "s", "-": "t", "..-": "u", ".--": "w", "...-": "v", "-..-": "x",
                        "-.--": "y", "--..": "z", "--..--": ",", ".-.-.-": ".", "..--..": "?", "-.-.--": "!"}


# This function translates a message into a morse code string
def message_to_morse(message):
    # Create an empty list variable
    char_list = list()
    # Loop through the message and put every character into the list variable
    for char in message:
        char_list += char.lower()

    morse_code = ""
    for char in char_list:
        if char == " ":
            morse_code += "   "
        elif char in to_morse_code_dict:
            translated_char = to_morse_code_dict[char]

            if morse_code == "":
                morse_code += translated_char
            else:
                morse_code += f" {translated_char}"
        else:
            morse_code = f"Can't convert char {char} to morse code"
            break

    return morse_code


# This function translates a morse code string into a message
def morse_to_message(morse):
    splitted_morse = morse.split(" ")
    emptys = 0
    message = ""
    for part in splitted_morse:
        if part == "":
            emptys += 1
            if emptys == 3:
                message += " "
                emptys = 0
        if part in from_morse_code_dict:
            translated_char = from_morse_code_dict[part]
            message += translated_char

    return message


def translate_text(text):
    is_morse = False
    for char in text:
        if char == "-" or char == ".":
            is_morse = True
            break
        elif char in to_morse_code_dict:
            break

    if is_morse:
        return morse_to_message(text)
    else:
        return message_to_morse(text)


if __name__ == "__main__":
    input_message = input("Enter an message to translate: ")
    print(translate_text(input_message))
