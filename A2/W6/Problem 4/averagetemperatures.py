# The required dataset for this program
temperatures = (
    ('1995', '3',
     ['47.3', '40.0', '38.3', '36.3', '37.4', '40.3', '41.1', '40.5', '41.6', '43.2', '46.2', '45.8', '44.9', '39.4',
      '40.5',
      '42.0', '46.5', '46.2', '43.3', '41.7', '40.7', '39.6', '44.2', '47.8', '45.9', '47.3', '39.8', '35.2', '38.5',
      '40.5', '47.0']),
    ('2010', '3',
     ['39.2', '36.7', '35.5', '35.2', '35.8', '33.8', '30.7', '33.2', '32.3', '33.3', '37.3', '39.9', '40.8', '42.9',
      '42.7',
      '42.6', '44.8', '50.3', '52.2', '55.2', '47.2', '45.0', '48.6', '55.0', '57.4', '50.9', '48.6', '46.2', '49.6',
      '50.1', '43.6']),
    ('2020', '3',
     ['43.2', '41.1', '40.0', '43.6', '42.6', '44.0', '44.0', '47.9', '46.6', '50.5', '51.5', '47.7', '44.7', '44.0',
      '48.9',
      '45.3', '46.6', '49.7', '47.2', '44.8', '41.8', '40.9', '41.0', '42.7', '43.4', '44.0', '46.4', '45.5', '40.7',
      '39.5', '40.6'])
)


def uniquetemperatures_task1():
    # Retrieve the 2 required years
    tempsinfo_1995 = temperatures[0]
    tempsinfo_2010 = temperatures[1]

    # Retrieve the temperatures for those years
    temps_1995 = tempsinfo_1995[2]
    temps_2010 = tempsinfo_2010[2]

    # Add both temperature lists together into one big list
    combined_temps = temps_1995 + temps_2010
    # Create an empty set variable
    unique_temps = set()

    # Loop through the combined_temps list and add all the unique tempratures to the list
    for temp in combined_temps:
        unique_temps.add(temp)

    # Return the length of the list
    return len(unique_temps)


def uniquetemperatures_task2():
    tempsinfo_1995 = temperatures[0]
    tempsinfo_2020 = temperatures[2]

    temps_1995 = tempsinfo_1995[2]
    temps_2020 = tempsinfo_2020[2]

    combined_temps = temps_1995 + temps_2020
    unique_temps = set()

    for temp in combined_temps:
        unique_temps.add(temp)

    return len(unique_temps)


def highesttemperature():
    tempsinfo_1995 = temperatures[0]
    tempsinfo_2010 = temperatures[1]
    tempsinfo_2020 = temperatures[2]

    temps_1995 = tempsinfo_1995[2]
    temps_2010 = tempsinfo_2010[2]
    temps_2020 = tempsinfo_2020[2]

    hottest_temp_1995 = 0.0
    for temp in temps_1995:
        float_temp = float(temp)
        if float_temp > hottest_temp_1995:
            hottest_temp_1995 = float_temp

    hottest_temp_2010 = 0.0
    for temp in temps_2010:
        float_temp = float(temp)
        if float_temp > hottest_temp_2010:
            hottest_temp_2010 = float_temp

    hottest_temp_2020 = 0.0
    for temp in temps_2020:
        float_temp = float(temp)
        if float_temp > hottest_temp_2020:
            hottest_temp_2020 = float_temp

    if hottest_temp_1995 > hottest_temp_2010 and hottest_temp_1995 > hottest_temp_2020:
        return "1995"
    elif hottest_temp_2010 > hottest_temp_1995 and hottest_temp_2010 > hottest_temp_2020:
        return "2010"
    elif hottest_temp_2020 > hottest_temp_1995 and hottest_temp_2020 > hottest_temp_2010:
        return "2020"
    else:
        return None


def warmest_march():
    tempsinfo_1995 = temperatures[0]
    tempsinfo_2010 = temperatures[1]
    tempsinfo_2020 = temperatures[2]

    temps_1995 = tempsinfo_1995[2]
    temps_2010 = tempsinfo_2010[2]
    temps_2020 = tempsinfo_2020[2]

    month_total_1995 = 0.0
    for temp in temps_1995:
        month_total_1995 += float(temp)

    month_total_2010 = 0.0
    for temp in temps_2010:
        month_total_2010 += float(temp)

    month_total_2020 = 0.0
    for temp in temps_2020:
        month_total_2020 += float(temp)

    if month_total_1995 > month_total_2010 and month_total_1995 > month_total_2020:
        return "1995"
    elif month_total_2010 > month_total_1995 and month_total_2010 > month_total_2020:
        return "2010"
    elif month_total_2020 > month_total_1995 and month_total_2020 > month_total_2010:
        return "2020"
    else:
        return None


if __name__ == "__main__":
    print(f"{uniquetemperatures_task1()}")
    print(f"{uniquetemperatures_task2()}")
    print(f"{highesttemperature()}")
    print(f"{warmest_march()}")
