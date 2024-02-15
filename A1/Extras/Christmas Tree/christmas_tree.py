# Make a function that generates the Christmas tree
def christmas_tree(tree_height):
    # Preform a check to see how high the tree is going to be to select a good-looking tree trunk size
    if tree_height <= 5:
        # Set how high and wide the tree trunk is going to be
        tree_trunk_height = 1
        tree_trunk_width = 1
        # Set the height of the leafs on tree
        tree_leaf_height = tree_height - tree_trunk_height
    elif tree_height <= 13:
        # Set how high and wide the tree trunk is going to be
        tree_trunk_height = 2
        tree_trunk_width = 3
        # Set the height of the leafs on tree
        tree_leaf_height = tree_height - tree_trunk_height
    else:
        # Set how high and wide the tree trunk is going to be
        tree_trunk_height = 3
        tree_trunk_width = 5
        # Set the height of the leafs on tree
        tree_leaf_height = tree_height - tree_trunk_height

    # Calculate the max width for the Christmas tree
    tree_leaf_max_width = 1
    i = 0
    while tree_leaf_height != i:
        tree_leaf_max_width += 2
        i += 1

    # Generate the Christmas tree leafs
    calc_leaf = 1
    e = 0
    while tree_leaf_height != e:
        str_leaf = ""

        # Calculate the amount of blank spaces are required for this step
        calc_spaces = int((tree_leaf_max_width - calc_leaf) / 2)

        # Preform a while loop to add the required blank spaces into the str_leaf variable
        a = 0
        while calc_spaces != a:
            str_leaf += " "
            a += 1

        # Preform a while loop to add the required amount of * into the str_leaf variable
        b = 0
        while calc_leaf != b:
            str_leaf += "*"
            b += 1

        e += 1
        calc_leaf += 2

        # Print the generated leaf row
        print(str(str_leaf))

    # Generate the tree trunk
    t = 0
    while tree_trunk_height != t:
        str_trunk = ""

        # Calculate the amount of blank spaces are required for this step
        calc_spaces = int((tree_leaf_max_width - tree_trunk_width) / 2)

        # Preform a while loop to add the required blank spaces into the str_trunk variable
        x = 0
        while calc_spaces != x:
            str_trunk += " "
            x += 1

        # Preform a while loop to add the required amount of * into the str_trunk variable
        c = 0
        while tree_trunk_width != c:
            str_trunk += "*"
            c += 1

        # Print the generated tree trunk row
        print(str_trunk)

        t += 1


# Request an input from the user to request the desired height
input_tree_height = input("Enter the height of the tree: ")
# Check if the input from the user is an integer
if input_tree_height.isdigit():
    # If the input is an integer, preform a check to see if it's higher than 1
    if int(input_tree_height) > 2:
        # If the input is an integer, preform the function required to generate the Christmas tree
        christmas_tree(int(input_tree_height))
    else:
        print("Invalid input, Please enter a number higher than 1 for the desired height of your christmas tree")
else:
    print("Invalid input, Please enter a number for the desired height of your christmas tree")
