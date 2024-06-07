hashmap_key_value = {}
encoded_values = []
decoded_values = []
default_key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"


def encode(char, key=default_key) -> str:
    # Create an empty dict in which we store the key for encoding
    encoding_dict = dict()

    # First preform a check to see if there is a key given when the function was called.
    # If not, check if there is already a dict_key_value.
    # And if that one also isn't filled, then use the default_key value
    if key is None:
        if hashmap_key_value == {}:
            key = default_key
        else:
            key = "use_dict_value"

    # Second, we check if we need to use the dict_key_value,
    # if we don't need to use this, then we will loop through the given key
    if key != "use_dict_value":
        # Use 2 pos values to make it possible to loop through the key value and extract the required values
        pos1 = 0
        pos2 = 1
        for i in range(int(len(key) / 2)):
            # Extract the key and the value from the key string
            key_key = key[pos1]
            key_value = key[pos2]

            # Check if the key has already been created in our dict, if not then we add the key and its value
            if key_key not in encoding_dict:
                encoding_dict[key_key] = key_value

            # Move the 2 pos variables to the next position
            pos1 += 2
            pos2 += 2
    else:
        encoding_dict = hashmap_key_value

    # Create an empty string in which we are going to store our encoded string
    return_data = ""

    # Third, we encode the data (string)
    if char not in encoding_dict:
        return_data += char
    else:
        return_data += encoding_dict[char]

    # After encoding, we add the encoded data to our encoded list and we return the result
    encoded_values.append(return_data)
    return return_data


def decode(char, key=default_key) -> str:
    # Create an empty dict in which we store the key for decoding
    decoding_dict = dict()

    # First preform a check to see if there is a key given when the function was called.
    # If not, check if there is already a dict_key_value.
    # And if that one also isn't filled, then use the default_key value
    if key is None:
        if hashmap_key_value == {}:
            key = default_key
        else:
            key = "use_dict_value"

    # Second, we check if we need to use the dict_key_value,
    # if we don't need to use this, then we will loop through the given key
    if key != "use_dict_value":
        # Use 2 pos values to make it possible to loop through the key value and extract the required values
        pos1 = 0
        pos2 = 1
        for i in range(int(len(key) / 2)):
            # Extract the key and the value from the key string
            key_key = key[pos1]
            key_value = key[pos2]

            # Check if the key has already been created in our dict, if not then we add the key and its value
            if key_key not in decoding_dict:
                decoding_dict[key_key] = key_value

            # Move the 2 pos variables to the next position
            pos1 += 2
            pos2 += 2
    else:
        decoding_dict = hashmap_key_value

    # Create an empty string in which we are going to store our decoded string
    return_data = ""

    # Third, we decode the data (string)
    decode_value_found = False
    for e in decoding_dict:
        if char == decoding_dict[e]:
            decode_value_found = True
            return_data += e
        if not decode_value_found:
            return_data += char

    # After encoding, we add the encoded data to our encoded list and we return the result
    decoded_values.append(return_data)
    return return_data


def encode_string(data: str, hofunction) -> str:
    return_value = ""

    for char in data:
        encoded_char = hofunction(char)
        return_value += encoded_char

    return return_value


def decode_string(data: str, hofunction) -> str:
    return_value = ""

    for char in data:
        decoded_char = hofunction(char)
        return_value += decoded_char

    return return_value


def encode_list(data: list, hofunction) -> list:
    # Create an empty return value list
    return_value = list()
    # Loop through the words in the data
    for item in data:
        # Encode the item with the High Order Function
        encoded_item = hofunction(item)
        # Add the encoded item to the return value list
        return_value.append(encoded_item)

    # Return the result
    return return_value


def decode_list(data: list, hofunction) -> list:
    # Create an empty return value list
    return_value = list()
    # Loop through the words in the data
    for item in data:
        # Decode the item with the High Order Function
        decoded_item = hofunction(item)
        # Add the decoded item to the return value list
        return_value.append(decoded_item)

    # Return the result
    return return_value


def validate_values(encoded: str, decoded: str, hofunction) -> bool:
    decoded_encoded_value = hofunction(encoded, hofunction)
    if decoded_encoded_value == decoded:
        return True
    else:
        return False


def print_menu():
    print("[E] Encode value to hashed value")
    print("[D] Decode hashed value to normal value")
    print("[P] Print all encoded/decoded values")
    print("[V] Validate 2 values against eachother")
    print("[Q] Quit program")


def main():
    while True:
        print_menu()
        input_menu_choice = input("Enter your choice: ").upper()
        if input_menu_choice == "Q":
            print("Exiting program, See you next time!")
            break
        elif input_menu_choice == "E":
            input_data = input("Enter a string for encoding: ")

            multi = False
            # Detect if there are multiple values to be encoded (Separated by comma)
            for char in input_data:
                if char == ",":
                    multi = True

            if multi:
                list_input_data = input_data.replace(" ", "").split(",")
                print(encode_list(list_input_data, encode))
            else:
                print(encode_string(input_data, encode))

        elif input_menu_choice == "D":
            input_data = input("Enter a string for decoding: ")

            multi = False
            # Detect if there are multiple values to be encoded (Separated by comma)
            for char in input_data:
                if char == ",":
                    multi = True

            if multi:
                list_input_data = input_data.replace(" ", "").split(",")
                print(decode_list(list_input_data, decode))
            else:
                print(decode_string(input_data, decode))

        elif input_menu_choice == "P":
            print("Encoded values:")
            for i in encoded_values:
                print(i)
            print("Decoded values:")
            for i in decoded_values:
                print(i)
        elif input_menu_choice == "V":
            input_encoded_value = input("Enter an encoded string: ")
            input_decoded_value = input("Enter an decoded string: ")
            print(validate_values(input_encoded_value, input_decoded_value, decode))
        else:
            print("Invalid input, please select an option.")


# Create an unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()
