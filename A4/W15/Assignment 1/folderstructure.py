def rec_print_folders(n: int, pref: str, root: list) -> None:
    pass


def rec_count_files(root: list) -> int:
    # Create a variable in which we will store our found files amount
    total_files_found = 0
    # Loop through the root
    for item in root:
        # Check if the instance is a list or a string
        if isinstance(item, list):
            # If it is a list, then rerun this function with the list as its argument
            total_files_found += rec_count_files(item)
        # If it is a file, then add 1
        elif isinstance(item, str):
            total_files_found += 1
        # Do nothing if it is anything else
        else:
            pass

    # Return the files found amount
    return total_files_found


if __name__ == "__main__":
    test_cases = [
        ['file_1', []],
        ['file_1', 'file_2', ['file_1']],
        ['file_1', 'file_2', ['file_3', 'file_4', 'file_5'], ['file_6', ['file_7', 'file_8'], ['file_9'], 'file_9', ['file_10']], []],
        ['file_1', ['file_3', ['file_2', ['file_10', ['file_9', 'file_8']]]], []],
        [[], [[], [[]]]]
    ]

    for case in test_cases:
        rec_print_folders(0, '', case)
        print('Number of files in case: ', case, ' is ', rec_count_files(case))
