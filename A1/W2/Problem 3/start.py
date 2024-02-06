# Request an input from the user
input_sides = int(input("Sides: "))

# With the switch case lookup which shape has that amount of sides
# If the integer is smaller than 3 or larger than 10
# Print an error message else print the shape

if input_sides < 3:
    print("Invalid input. Please enter an number between 3 and 10")
elif input_sides == 3:
    print('Triangle')
elif input_sides == 4:
    print('Squar')
elif input_sides == 5:
    print('Pentagon')
elif input_sides == 6:
    print('Hexagon')
elif input_sides == 7:
    print('Heptagon')
elif input_sides == 8:
    print('Octagon')
elif input_sides == 9:
    print('Nonagon')
elif input_sides == 10:
    print('Decagon')
else:
    print("Invalid input. Please enter an number between 3 and 10")
