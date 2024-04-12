# Import the predefined dictionary
dict_catalog = {'A': {3: 8, 8: 24, 10: 37},
                'B': {3: 7, 7: 19, 16: 88, 20: 135, 100: 3342},
                'C': {3: 8,   7: 17,    16: 92,   20: 136,   100: 3343},
                'D': {3: 8,   6: 15,    9: 29,    16: 90,    25: 216},
                'E': {6: 15,  9: 32,    25: 214,  30: 304},
                'F': {6: 21,  9: 37,    25: 215,  30: 306},
                'G': {6: 18,  9: 29,    25: 214,  30: 310},
                'H': {3: 11,  8: 30,    10: 43},
                'I': {3: 11,  7: 24,    16: 94,   20: 136,   100: 3338},
                'J': {3: 6,   7: 25,    16: 91,   20: 138,   100: 3339},
                'K': {6: 17,  9: 37,    25: 213,  30: 307},
                'L': {3: 13,  7: 24,    16: 94,   20: 137,   100: 3343},
                'M': {3: 7,   7: 22,    16: 88,   20: 135,   100: 3340},
                'N': {6: 19,  9: 28,    25: 215,  30: 301},
                'O': {3: 6,   7: 24,    16: 93,   20: 138,   100: 3336},
                'P': {6: 17,  9: 33,    25: 212,  30: 306},
                'Q': {50: 836,      100: 3343,         150: 7504},
                'R': {6: 16,  9: 37,    25: 209,  30: 310},
                'S': {50: 834,   100: 3339,   150: 7510},
                'T': {50: 839,   100: 3336,   150: 7505},
                'U': {3: 6,    7: 25,     16: 87,    20: 137,     100: 3336},
                'V': {3: 10,   6: 22,      9: 36,     16: 94,       25: 209},




                'W': {6: 18,    9: 29,      25: 217,       30: 301},






                'X': {3: 8, 7: 18, 16: 92, 20: 138, 100: 3338},
                'Y': {50: 843, 100: 3335, 150: 7508},
                'Z': {50: 839, 100: 3334, 150: 7501}}

# Import the predefined collection list
collection = ['M100', 'O20', 'T50', 'M20', 'U7', 'G25', 'H3', 'K25', 'W9',
              'L7', 'V6', 'L100', 'I16', 'H8', 'E6', 'O3', 'L20', 'J20',
              'Y50', 'E25', 'C7', 'D6', 'S150', 'F6', 'T150', 'U16', 'V25',
              'S50', 'J7', 'W25', 'R30', 'S100', 'F9', 'U20', 'W6', 'A3',
              'P9', 'I100', 'U3', 'D9', 'F25', 'R6', 'J16', 'H10', 'I3',
              'X7', 'Y150', 'C100', 'A10', 'O16', 'G6', 'N9', 'N25', 'N6',
              'Q150', 'M7', 'D16', 'I20', 'M16', 'P6', 'V3', 'C16', 'R9',
              'L3', 'E9', 'A8', 'G30', 'C3', 'C20', 'Z50', 'D25', 'K30',
              'X20', 'V16', 'G9', 'M3', 'O100', 'Z150', 'O7', 'V9']

collection_inventory = {'A': {3: 0, 8: 0, 10: 0},
                        'B': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'C': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'D': {3: 0, 6: 0, 9: 0, 16: 0, 25: 0},
                        'E': {6: 0, 9: 0, 25: 0, 30: 0},
                        'F': {6: 0, 9: 0, 25: 0, 30: 0},
                        'G': {6: 0, 9: 0, 25: 0, 30: 0},
                        'H': {3: 0, 8: 0, 10: 0},
                        'I': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'J': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'K': {6: 0, 9: 0, 25: 0, 30: 0},
                        'L': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'M': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'N': {6: 0, 9: 0, 25: 0, 30: 0},
                        'O': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'P': {6: 0, 9: 0, 25: 0, 30: 0},
                        'Q': {50: 0, 100: 0, 150: 0},
                        'R': {6: 0, 9: 0, 25: 0, 30: 0},
                        'S': {50: 0, 100: 0, 150: 0},
                        'T': {50: 0, 100: 0, 150: 0},
                        'U': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'V': {3: 0, 6: 0, 9: 0, 16: 0, 25: 0},
                        'W': {6: 0, 9: 0, 25: 0, 30: 0},
                        'X': {3: 0, 7: 0, 16: 0, 20: 0, 100: 0},
                        'Y': {50: 0, 100: 0, 150: 0},
                        'Z': {50: 0, 100: 0, 150: 0}}

collection_value = 0

for item in collection:
    catalog = item[0]
    catalog_part = int(item[1:(len(item))])
    if catalog in dict_catalog:
        dict_of_catalog_stamps = dict_catalog[catalog]
        if catalog_part in dict_of_catalog_stamps:
