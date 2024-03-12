if __name__ == "__main__":
    # This function preforms a check to see if the unchecked string is an integer
    def is_integer(unchecked: str):
        is_int = "Invalid"
        try:
            input_float = float(unchecked)
            if input_float >= 1 and input_float == round(input_float, 0):
                is_int = "Valid"
        except ValueError:
            print(ValueError)
        return is_int

    # This function preforms a check to see if the unchecked string is an integer
    def remove_non_integer(unchecked: str):
        input_str = unchecked
        is_a_minus = False
        numbers = ""

        for i in input_str:
            if i == input_str[0] and i == "-":
                is_a_minus = True
            elif i.isnumeric():
                numbers += i
            else:
                pass

        number = int(numbers)
        if is_a_minus:
            number = number - (number * 2)
        return number


else:
    # This function preforms a check to see if the unchecked string is an integer
    def is_integer(unchecked: str):
        is_int = "Invalid"
        try:
            input_float = float(unchecked)
            if input_float >= 1 and input_float == round(input_float, 0):
                is_int = "Valid"
        except ValueError:
            print(ValueError)
        return is_int

    # This function preforms a check to see if the unchecked string is an integer
    def remove_non_integer(unchecked: str):
        input_str = unchecked
        is_a_minus = False
        numbers = ""

        for i in input_str:
            if i == input_str[0] and i == "-":
                is_a_minus = True
            elif i.isnumeric():
                numbers += i
            else:
                pass

        number = int(numbers)
        if is_a_minus:
            number = number - (number * 2)
        return number
