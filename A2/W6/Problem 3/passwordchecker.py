def password_check():
    chances_used = 0
    while chances_used != 3:
        input_user = input("Enter : ")
        validation_results = password_validion(input_user)

        if validation_results:
            print("Password is valid")
            break
        else:
            print("Password is invalid")
            chances_used += 1


def password_validion(password: str):
    sets = set()

    for char in password:
        sets.add(char)

    if 8 <= len(password) <= 19:
        acii_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        acii_lowercase = "abcdefghijklmnopqrstuvwxyz"
        acii_digits = "0123456789"
        allowed_symbols = "*@!?"
        total_allowed_list = acii_uppercase + acii_lowercase + acii_digits + allowed_symbols

        valids = 0
        invalids = 0

        for set_value in sets:
            if set_value not in total_allowed_list:
                invalids += 1
            else:
                valids += 1

        if valids == len(sets) and invalids == 0:
            return True
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    password_check()
