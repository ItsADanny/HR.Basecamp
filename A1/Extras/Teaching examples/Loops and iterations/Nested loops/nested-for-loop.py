triangle_height = 5
max_triangle_width = 0

# EN : First calculate the maximum width of the triangle
# NL : Bereken eerst de maximum breedte van de driehoek
for i in range(triangle_height):
    max_triangle_width += 2

calc_triangle = 1
for e in range(triangle_height):
    str_triangle_row = ""

    # EN : Calculate the amount of spaces that are required for this step
    # NL : Bereken eerst de benodigde spaties voor deze stap
    calc_spaces = int((max_triangle_width - calc_triangle) / 2)

    # EN : Preform a while loop to add the required blank spaces into the str_triangle_row variable
    # NL : Doe een While loop om het benodigde aantal spaties alvast toe tevoegen aan de str_triangle_row variable
    for s in range(calc_spaces):
        str_triangle_row += " "

    # EN : Preform a while loop to add the required amount of * into the str_triangle_row variable
    # NL : Doe een While loop om de benodigde aantal * toe tevoegen aan de str_triangle_row variable
    for o in range(calc_triangle):
        str_triangle_row += "*"

    calc_triangle += 2

    # EN : Print the generated the row
    # NL : Print de regel
    print(str_triangle_row)
