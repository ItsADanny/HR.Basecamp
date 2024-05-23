def rec_print_folders(n: int, pref: str, root: list) -> None:
    '''
    This function prints the contents of a given root folder with indentations.
    '''
	# todo: implement the body of this function

def rec_count_files(root: list) -> int:
	'''
	The functions counts number of files in a given folder (and all its sub-folders).
	:param root: A nested list: an element either is a file (name) or a list as a sub-folder.
	:return:
	'''
	# todo: implement the body of this function


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