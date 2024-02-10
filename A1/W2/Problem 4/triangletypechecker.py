__author__ = 'Danny de Snoo, HR-nr: 1091749'

# import a function to turn a list into a array
from array import array

# request an input from the user
input_triangle = input("")

if "," in input_triangle:
    array_triangle = input_triangle.split()
    numbers = array("i", array_triangle)


else:
    print("Please input a valid triangle.")
