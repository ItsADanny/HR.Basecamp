# Import the required module
import string


def password_checker(password: str):
    sets = set()

    for char in password:
        sets.add(char)

    if 7 <= len(sets) <= 19:
        acii_uppercase = string.ascii_uppercase
        acii_lowercase = string.ascii_lowercase
        acii_digits = string.digits
        allowed_symbols = "*@!?"
        total_allowed_list = acii_uppercase + acii_lowercase + acii_digits + allowed_symbols

        valids = 0
        invalids = 0

        print(f"sets : {sets}")

        for set_value in sets:
            if set_value not in allowed_symbols:
                valids += 1
            else:
                invalids += 1

        print(f"valids : {valids}")
        print(f"invalids : {invalids}")

        if valids == len(sets) and invalids == 0:
            return True
        else:
            return False
    else:
        return False


input_user = input("Enter : ")
print(f"password_checker : {password_checker(input_user)}")
