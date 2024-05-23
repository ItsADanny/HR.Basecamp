hashmap_key_value = {}
encoded_values = []
decoded_values = []
default_key = "a_b?c9d6e1f4g!h:i<j|k{l0m@n7o+p~q2r+s/t=u^v3w]x(y-z>A*B8C;D%E#F}G5H)I[J$"

def encode(char, key) -> str:
    



def decode(char, key) -> str:

def encode_string(data: str, hofunction) -> str:
    return_value = ""

    for char in data:
        encoded_char = hofunction(char)
        return_value += encoded_char

    return return_value


def decode_string(data: str, hofunction) -> str:
    raise NotImplementedError


def encode_list(data: list, hofunction) -> list:
    raise NotImplementedError


def decode_list(data: list, hofunction) -> list:
    raise NotImplementedError


def validate_values(encoded: str, decoded: str, hofunction) -> bool:
    raise NotImplementedError


def main():
    raise NotImplementedError


# Create a unittest for both the encode and decode function (see test_namehasher.py file for boilerplate)
if __name__ == "__main__":
    main()
