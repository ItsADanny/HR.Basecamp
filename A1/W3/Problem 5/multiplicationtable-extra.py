# Here you can input the max number that you want the multiplication to go up to
max_num_width = 10
max_num_height = 10

curr_pos_width = 0
curr_pos_height = 0
str_row = ""

while curr_pos_height != (max_num_height + 1):
    # If it's the first row create a header for the table with a while loop
    if curr_pos_height == 0:
        str_row += " "
        while curr_pos_width != max_num_width:
            curr_pos_width += 1
            # If it's the final position, add the number with just 1 space else use 2 spaces
            if curr_pos_width == max_num_width:
                str_row += f" {curr_pos_width}"
            else:
                str_row += f"  {curr_pos_width}"
    # If it's under the header preform a slightly different while loop
    else:
        str_row += f"{curr_pos_height}"
        while curr_pos_width != max_num_width:
            # Calculate the multiplication for that position
            calc_num = curr_pos_height * (curr_pos_width + 1)

            # Check to see how long the number is, if it's 1 character long then add 2 spaces else add 1
            if len(str(calc_num)) == 1:
                str_row += f"  {calc_num}"
            else:
                str_row += f" {calc_num}"

            # Update the current width position by 1
            curr_pos_width += 1

    # Print the row, reset the row string, update the current height position by 1 and reset the current width position
    print(str_row)
    str_row = ""
    curr_pos_height += 1
    curr_pos_width = 0
