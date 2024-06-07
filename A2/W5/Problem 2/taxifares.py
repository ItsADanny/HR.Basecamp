def calculate_fare(distance):
    # Turn the given distance (Kilometers) to Meters
    meters = distance * 1000

    # Set the base fare
    base_fare = 4.00
    # Calculate the amount_times based on a certain number of meters
    times_amount = meters / 140

    # Preform a check if the amount_times isn't a number with a decimal. If so, round it up.
    if times_amount > round(times_amount, 0):
        times_amount = round(times_amount, 0) + 1

    # Preform the times in which we do the number of 140 meter times 0.25
    fare_meterprice = times_amount * 0.25
    # Add the result from above to the base rate
    total_fare = base_fare + fare_meterprice

    # Return the results
    return total_fare


if __name__ == '__main__':
    # Request an input from the user and then print the results from the function
    input_kilometers = input("Distance traveled: ")
    if input_kilometers.isdigit() and float(input_kilometers) >= 0:
        print(f"Total fare: {round(calculate_fare(float(input_kilometers)), 2)}")
    else:
        print("Invalid input")
