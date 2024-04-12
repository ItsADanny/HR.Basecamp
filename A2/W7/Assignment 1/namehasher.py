# Import the required modules
import hashlib

# Global variables
dict_key_value = {}
encoded_values = []
decoded_values = []


def program():
    running = True
    while running:
        # Print the menu after each action
        print_menu()
        # Request an input from the user
        input_user_selection = input("")
        # Check if the input is a alphabetic character
        if input_user_selection.isalpha():
            # Turn the input from the user into an uppercase character
            input_user_selection = input_user_selection.upper()
            # Check if the input from the user is valid
            if input_user_selection == "E":
                input_user_to_encode = input("Enter : ")
                encoded_str = encode_string(input_user_to_encode)
                print(encoded_str)
            elif input_user_selection == "D":
                input_user_to_decode = input("Enter : ")
                decoded_str = decode_string(input_user_to_decode)
                print(decoded_str)
            elif input_user_selection == "P":
                print("========================================")
                print("ENCODED VALUES")
                for e in encoded_values:
                    print(e)
                print("========================================")
                print("DECODED VALUES")
                for d in decoded_values:
                    print(d)
                print("========================================")
            elif input_user_selection == "V":
                pass
            elif input_user_selection == "Q":
                print("Exiting program")
                running = False
            else:
                print("Invalid input, Please select a valid option")
        else:
            print("Invalid input, Please select a valid option")


def print_menu():
    print('[E] Encode value to hashed value')
    print('[D] Decode hashed value to normal value')
    print('[P] Print all encoded/decoded values')
    print('[V] Validate 2 values against eachother')
    print('[Q] Quit program\n\n')


def encode_string(data: str, key: str = None) -> str:
    encoded_data = []

    for item in data:
        encoded_data.append(encode_string(item, key))

    return encoded_data


def decode_string(data: str, key: str = None) -> str:
    decoded_data = []

    for item in data:
        decoded_data.append(decode_string(item, key))

    return decoded_data


def encode_list(data: list, key: str = None) -> list:
    encoded_data = []

    for item in data:
        encoded_data.append(encode_string(item, key))

    return encoded_data


def decode_list(data: list, key: str = None) -> list:
    decoded_data = []

    for item in data:
        decoded_data.append(decode_string(item, key))

    return decoded_data


def validate_values(encoded: str, decoded: str, key: str = None) -> bool:
    pass


def set_dict_key(conversion_string: str) -> None:
    pass


program()

if __name__ == "__main__":
    program()
