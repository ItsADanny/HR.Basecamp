finished = False
Pos = 0
Possibilities = 0
ImPossibilities = 0
curr_pincode = 0

while not finished:
    pincode_length = len(str(curr_pincode))
    pincode = ""

    if pincode_length != 6:
        missing_length = 6 - pincode_length
        for i in range(missing_length):
            pincode += "0"

        pincode = pincode + str(curr_pincode)
    else:
        pincode = str(curr_pincode)

    # print(pincode)

    pincode_part1 = pincode[0]
    pincode_part2 = pincode[1]
    pincode_part3 = pincode[2]
    pincode_part4 = pincode[3]
    pincode_part5 = pincode[4]
    pincode_part6 = pincode[5]

    valid_sum_check_1 = False
    valid_sum_check_2 = False
    valid_sum_check_3 = False
    valid_sum_check_4 = False
    valid_sum_check_5 = False

    if pincode_part1 != pincode_part2:
        valid_sum_check_1 = True
    if pincode_part2 != pincode_part3:
        valid_sum_check_2 = True
    if pincode_part3 != pincode_part4:
        valid_sum_check_3 = True
    if pincode_part4 != pincode_part5:
        valid_sum_check_4 = True
    if pincode_part5 != pincode_part6:
        valid_sum_check_5 = True

    double_check_dict = {}
    for num in pincode:
        if num not in double_check_dict:
            double_check_dict[num] = 1
        else:
            double_check_dict[num] = double_check_dict[num] + 1

    invalid_letteramount = 0
    for check in double_check_dict:
        letter = check
        value = double_check_dict[check]
        if value > 2:
            invalid_letteramount += 1

    if valid_sum_check_1 and valid_sum_check_2 and valid_sum_check_3 and valid_sum_check_4 and valid_sum_check_5 and invalid_letteramount == 0:
        Possibilities += 1
    else:
        ImPossibilities += 1

    if curr_pincode == 999999:
        finished = True

    curr_pincode += 1

print(f"Possibilities   : {Possibilities}")
print(f"ImPossibilities : {ImPossibilities}")