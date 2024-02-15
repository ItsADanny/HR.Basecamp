__author__ = 'Danny de Snoo, HR-nr: 1091749'

# request an input from the user
input_triangle = input("Sides: ")

int_differences = 0

# First we remove all the white spaces
stripped_input_triangle = input_triangle.strip()
# Remove the "a=", "b=", "c=" and ,
stripped_input_triangle = stripped_input_triangle.replace("a=", "")
stripped_input_triangle = stripped_input_triangle.replace("b=", "")
stripped_input_triangle = stripped_input_triangle.replace("c=", "")
stripped_input_triangle = stripped_input_triangle.replace(",", "")
# Then split the stripped input
splitted_input_triangle = stripped_input_triangle.split()

# retrieve the value from the array and put in it into a variable
int_side1 = splitted_input_triangle[0]
int_side2 = splitted_input_triangle[1]
int_side3 = splitted_input_triangle[2]

# Preform the check to see which traingle type it is
if int_side1 == int_side2 == int_side3:
    # if all sides are the same then print:
    print("equilateral triangle")
else:
    if int_side1 == int_side2 or int_side1 == int_side3 or int_side2 == int_side3:
        # if only 2 sides are the same then print:
        print("isosceles triangle")
    else:
        # and if all the sides are unique print:
        print("scalene triangle")
