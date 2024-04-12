roman_integers_list = ["DXXXIV", "MXXVII", "CLXXVII", "CMXXV", "CCCXIII", "CDLXXXIII", "MCCCL", "MCCLXV", "MDXX", "DCLIII", "DCCCLVII", "MDCXC", "VII", "MLXI", "MCDXVIII", "DCCXXXVIII", "LVIII", "MDCLXXIII", "MCDLXXXVI", "MCCCLXXXIV", "XCII", "DLXXXV", "DCLXXXVII", "DCCCXCI", "DCXXXVI", "MCLXXX", "DXVII", "CCXXVIII", "MCCXIV", "CCCXCVIII", "DCCIV", "CCLXXIX", "DCXIX", "MCCXXXI", "CXCIV", "CIX", "DCCCXL", "MCXLVI", "DCCLV", "CXLIII", "MCCCLXVII", "CMLIX", "MCCLXXXII", "MCLXIII", "MDCLVI", "CCLXII", "MDLXXI", "DCCCXXIII", "CDLXVI", "MCDXXXV", "MXLIV", "MXCV", "CCXCVI", "MDIII", "CXXVI", "DCCXXI", "MCCCXVI", "DCCCVI", "MDXXXVII", "DCCLXXXIX", "MDCXXII", "MLXXVIII", "MCDLXIX", "DCLXX", "CDXLIX", "CMVIII", "MCDLII", "MDCV", "CCCXXX", "CMLXXVI", "CCCLXXXI", "MDLIV", "MCXXIX", "MX", "MCCXLVIII", "MCDI", "MCXCVII", "MCCCXXXIII", "MCXII", "CDXV", "CMXLII", "MDLXXXVIII", "DLI", "CCCLXIV", "CCXLV", "DCCCLXXIV", "CCCXLVII", "XLI", "XXIV", "CDXXXII", "DCCLXXII", "CCXI", "DLXVIII", "LXXV", "MDCXXXIX", "CLX", "DCII", "MCCXCIX", "CMXCIII"]


def roman_to_int():
    list_int = []
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for roman_num in roman_integers_list:
        number = 0
        prev_value = 0

        for numeral in reversed(roman_num):
            value = roman[numeral]
            if value < prev_value:
                number -= value
            else:
                number += value
            prev_value = value

        list_int.append(number)

    return list_int


def check_difference(input_list):
    curr_pos = 0
    next_pos = 1

    for number in input_list:
        curr_number = input_list[curr_pos]
        next_number = input_list[next_pos]

        if (curr_number + 17) != next_number:
            return curr_number + 17

        curr_pos += 1
        next_pos += 1


convertedlist = roman_to_int()
missing_number = check_difference(convertedlist)
print(missing_number)