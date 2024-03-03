triangle_height = 5
max_triangle_width = 0

# EN : First calculate the maximum width of the triangle
# NL : Bereken eerst de maximum breedte van de driehoek
i = 0
while triangle_height != i:
    max_triangle_width += 2
    i += 1

calc_triangle = 1
e = 0
while triangle_height != e:
    str_triangle_row = ""

    # EN : Calculate the amount of spaces that are required for this step
    # NL : Bereken eerst de benodigde spaties voor deze stap
    calc_spaces = int((max_triangle_width - calc_triangle) / 2)

    # EN : Preform a while loop to add the required blank spaces into the str_triangle_row variable
    # NL : Doe een While loop om het benodigde aantal spaties alvast toe tevoegen aan de str_triangle_row variable
    a = 0
    while calc_spaces != a:
        str_triangle_row += " "
        a += 1

    # EN : Preform a while loop to add the required amount of * into the str_triangle_row variable
    # NL : Doe een While loop om de benodigde aantal * toe tevoegen aan de str_triangle_row variable
    b = 0
    while calc_triangle != b:
        str_triangle_row += "*"
        b += 1

    e += 1
    calc_triangle += 2

    # EN : Print the generated the row
    # NL : Print de regel
    print(str(str_triangle_row))
