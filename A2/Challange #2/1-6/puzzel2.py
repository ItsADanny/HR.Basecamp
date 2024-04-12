class Register:
    def __init__(self, reqister_name):
        self.register = reqister_name
        self.value = 100


def load(part_1: Register, part_2: str):
    load_value = 0

    if part_2.isnumeric():
        load_value = int(part_2)
    else:
        register_2 = None
        for reg in registers:
            if reg.register == part_2:
                register_2 = reg

        load_value = register_2.value

    part_1.value = load_value


def add(part_1: Register, part_2: str):
    part_2_value = 0

    if part_2.isnumeric():
        part_2_value = int(part_2)
    else:
        register_2 = None
        for reg in registers:
            if reg.register == part_2:
                register_2 = reg

        part_2_value = register_2.value

    part_1.value += part_2_value


def sub(part_1: Register, part_2: str):
    part_2_value = 0

    if part_2.isnumeric():
        part_2_value = int(part_2)
    else:
        register_2 = None
        for reg in registers:
            if reg.register == part_2:
                register_2 = reg

        part_2_value = register_2.value

    part_1.value -= part_2_value


def mul(part_1: Register, part_2: str):
    if part_2.isnumeric():
        part_2_value = int(part_2)
        part_1.value = part_2_value * part_1.value
    else:
        register_2 = None
        for reg in registers:
            if reg.register == part_2:
                register_2 = reg

        register_2_value = register_2.value
        part_1.value = part_1.value * register_2_value


instructions = [["ADD", "S", "Z"],
                ["ADD", "Z", "18"],
                ["SUB", "D", "P"],
                ["SUB", "P", "67"],
                ["MUL", "U", "M"],
                ["MUL", "M", "36"],
                ["LOAD", "P", "A"],
                ["LOAD", "A", "59"],
                ["MUL", "T", "Y"],
                ["MUL", "Y", "10"],
                ["MUL", "I", "X"],
                ["MUL", "X", "39"],
                ["LOAD", "K", "A"],
                ["LOAD", "A", "12"],
                ["LOAD", "U", "R"],
                ["LOAD", "R", "11"],
                ["MUL", "V", "G"],
                ["MUL", "G", "64"],
                ["LOAD", "Q", "H"],
                ["LOAD", "H", "66"],
                ["MUL", "R", "H"],
                ["MUL", "H", "54"],
                ["ADD", "V", "H"],
                ["ADD", "H", "68"],
                ["SUB", "A", "N"],
                ["SUB", "N", "81"],
                ["LOAD", "F", "U"],
                ["LOAD", "U", "47"],
                ["LOAD", "X", "K"],
                ["LOAD", "K", "74"],
                ["MUL", "Q", "V"],
                ["MUL", "V", "34"],
                ["SUB", "J", "S"],
                ["SUB", "S", "73"],
                ["MUL", "S", "B"],
                ["MUL", "B", "71"],
                ["ADD", "X", "Z"],
                ["ADD", "Z", "61"],
                ["MUL", "V", "F"],
                ["MUL", "F", "56"],
                ["SUB", "C", "O"],
                ["SUB", "O", "94"],
                ["LOAD", "Y", "F"],
                ["LOAD", "F", "76"],
                ["MUL", "L", "P"],
                ["MUL", "P", "13"],
                ["MUL", "B", "J"],
                ["MUL", "J", "88"],
                ["MUL", "U", "F"],
                ["MUL", "F", "31"],
                ["ADD", "A", "Y"],
                ["ADD", "Y", "35"],
                ["ADD", "M", "Q"],
                ["ADD", "Q", "54"],
                ["SUB", "O", "I"],
                ["SUB", "I", "94"],
                ["LOAD", "M", "Z"],
                ["LOAD", "Z", "75"],
                ["ADD", "Q", "Y"],
                ["ADD", "Y", "81"],
                ["ADD", "N", "B"],
                ["ADD", "B", "71"],
                ["SUB", "S", "R"],
                ["SUB", "R", "35"],
                ["MUL", "P", "L"],
                ["MUL", "L", "63"],
                ["SUB", "A", "R"],
                ["SUB", "R", "79"],
                ["SUB", "O", "T"],
                ["SUB", "T", "13"],
                ["ADD", "U", "F"],
                ["ADD", "F", "80"],
                ["ADD", "C", "Z"],
                ["ADD", "Z", "80"],
                ["SUB", "B", "V"],
                ["SUB", "V", "19"],
                ["LOAD", "A", "O"],
                ["LOAD", "O", "11"],
                ["SUB", "H", "I"],
                ["SUB", "I", "24"],
                ["ADD", "L", "J"],
                ["ADD", "J", "18"],
                ["ADD", "F", "I"],
                ["ADD", "I", "77"],
                ["ADD", "V", "I"],
                ["ADD", "I", "92"],
                ["SUB", "O", "W"],
                ["SUB", "W", "51"],
                ["MUL", "P", "D"],
                ["MUL", "D", "13"],
                ["SUB", "M", "K"],
                ["SUB", "K", "63"],
                ["ADD", "I", "D"],
                ["ADD", "D", "42"],
                ["ADD", "T", "N"],
                ["ADD", "N", "12"],
                ["ADD", "A", "M"],
                ["ADD", "M", "28"],
                ["LOAD", "X", "F"],
                ["LOAD", "F", "67"]]
registers_str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
registers = []

for register in registers_str:
    new_register = Register(register)
    registers.append(new_register)


for instruction in instructions:
    task_instruction = instruction[0]
    task_register = instruction[1]
    task_value = instruction[2]

    acting_register = None
    for reg in registers:
        if reg.register == task_register:
            acting_register = reg

    if task_instruction == "LOAD":
        load(acting_register, task_value)
    if task_instruction == "ADD":
        add(acting_register, task_value)
    if task_instruction == "SUB":
        sub(acting_register, task_value)
    if task_instruction == "MUL":
        mul(acting_register, task_value)


highest_register = ""
highest_register_value = 0
for register in registers:
    # DEBUGGING
    # print("-------------------------")
    # print(f"Register : {register.register}")
    # print(f"Value    : {register.value}")

    if register.value > highest_register_value:
        highest_register = register.register
        highest_register_value = register.value

print(f"highest register : {highest_register}")
print(f"register value   : {highest_register_value}")