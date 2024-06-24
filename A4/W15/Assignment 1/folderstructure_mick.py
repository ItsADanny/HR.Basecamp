def rec_print_folders(n: int, pref: str, root: list) -> None:
    '''
    This function prints the contents of a given root folder with indentations.
    '''
    current_folder = n
    data = []
    for item in root:
        if isinstance(item, list):
            # files += rec_count_files(item)
            pass
        elif isinstance(item, str):
            # files += 1
            pass
        else:
            pass


# todo: implement the body of this function

def rec_count_files(root: list) -> int:
    files = 0
    for item in root:
        if isinstance(item, list):
            files += rec_count_files(item)
        elif isinstance(item, str):
            files += 1
        else:
            pass

    return files

if __name__ == "__main__":
    test_cases = [
        ['file_1', []],
        ['file_1', 'file_2', ['file_1']],
        ['file_1', 'file_2', ['file_3', 'file_4', 'file_5'],
         ['file_6', ['file_7', 'file_8'], ['file_9'], 'file_9', ['file_10']], []],
        ['file_1', ['file_3', ['file_2', ['file_10', ['file_9', 'file_8']]]], []],
        [[], [[], [[]]]]
    ]

    for case in test_cases:
        rec_print_folders(0, '', case)
        print('Number of files in case: ', case, ' is ', rec_count_files(case))