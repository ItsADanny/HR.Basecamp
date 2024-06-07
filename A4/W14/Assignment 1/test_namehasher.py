from namehasher import encode_string, decode_string, encode_list, decode_list, validate_values


def encode_decode_function(data) -> str:
    result = ""
    hash = dict(zip(*[iter("A%B&C(D)E*F+G-H/I0J<K=L1M!N9O?P>Q7R#S5T;U:V[W]X~Y$Z@")]*2))

    if data[:3] == "_E$":
        data = data[3:]
        hash = {v: k for k, v in hash.items()}
    else:
        result += "_E$"

    for char in data:
        result += (char if char not in hash else hash[char])

    return result


def test_encode_string():
    # check if given the hashmap string, the correct output is given
    assert "_E$**9 (?##*(;* :0;=?!5;" == encode_string("EEN CORRECTE UITKOMST", encode_decode_function)
    # check if case insesitive input is handle correctly
    assert "_E$*en (orrecte :itkomst" == encode_string("Een Correcte Uitkomst", encode_decode_function)


def test_decode_string():
    # check if given hasmap string, the correct decode output is given
    assert "ANDERSOM WERKT OOK" == decode_string("_E$%9)*#5?! ]*#=; ??=", encode_decode_function)
    # check if case insesitive input is handle correctly
    assert "Ook Met Kleine Letters" == decode_string("_E$?ok !et =leine 1etters", encode_decode_function)


def test_encode_list():
    # check if given a list of values the encoded output is a list of encoded values
    assert ["_E$>0*;*#", "_E$>%9"] == encode_list(["PIETER", "PAN"], encode_decode_function)


def test_decode_list():
    # check if given a list of values the decoded output is a list of decoded values
    assert ["PIETER", "PAN"] == decode_list(["_E$>0*;*#", "_E$>%9"], encode_decode_function)


def test_validate_values():
    # check if the given values are equal based on the provided hashmap
    assert True == validate_values("_E$>0*;*#", "PIETER", encode_decode_function)
    # check if the given values are not equal based on case sensitivity and the provided hashmap
    assert False == validate_values("_E$>0*;*#", "Pieter", encode_decode_function)
