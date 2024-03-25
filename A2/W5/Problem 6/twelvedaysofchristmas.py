def next_verse(vers_number: int):
    # Create 2 list which contain the gifts and a list that contains the days
    item_list = ["A partridge in a pear tree", "Two turtle doves", "Three French hens", "Four calling birds", "Five golden rings", "Six geese a-laying", "Seven swans a-swimming", "Eight maids a-milking", "Nine ladies dancing", "Ten lords a-leaping", "Eleven pipers piping", "Twelve drummers drumming"]
    days_list = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"]

    # Create a empty item string in which we will store all the given gift for that day
    item_str = ""
    # Preform a for-loop in which we loop over a range of the current days + 1
    for e in range((vers_number + 1)):
        if item_str == "":
            item_str += item_list[e]
        else:
            if e != vers_number:
                item_str = item_list[e] + ", " + item_str
            else:
                # item_str = item_str + " and " + item_list[e]
                item_str = item_list[e] + " and " + item_str

    # Retriev the selected day
    day = days_list[vers_number]

    # Print the result
    print(f"On the {day} day of Christmas, my true love sent to me {item_str}")

# Preform a loop to generate the results
for i in range(12):
    next_verse(i)
