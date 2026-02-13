"""
-------------------------------------------------------
Assignment 4, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-10-13"
-------------------------------------------------------
"""

# task 1


def day_name(day_num):
    """
    -------------------------------------------------------
    Returns the name of a day of the week given an integer day number.
    Day 1 is "Sunday", day 7 is "Saturday".
    Returns "Error" if the number is not valid.
    Use: day = day_name(day_num)
    -------------------------------------------------------
    Parameters:
        day_num - day number (1 <= int <= 7)
    Returns:
        day - name of a day of the week (str)
    ------------------------------------------------------
    """
    if day_num == 1:
        day = "Sunday"

    elif day_num == 2:
        day = ("Monday")

    elif day_num == 3:
        day = ("Tuesday")

    elif day_num == 4:
        day = ("Wednesday")

    elif day_num == 5:
        day = ("Thursday")

    elif day_num == 6:
        day = ("Friday")

    elif day_num == 7:
        day = ("Saturday")

    return day

# task 2


def pollution_ranking(air_quality_index):
    """
    -------------------------------------------------------
    Returns the pollution level given an AQI (Air Quality Index):
        "Good" - 0 to 50 AQI
        "Moderate" - 51 - 100 AQI
        "Unhealthy for Sensitive Groups" - 101 - 150 AQI
        "Unhealthy" - 151 - 200 AQI
        "Very Unhealthy" - 201 - 300 AQI
        "Hazardous" - 300+ AQI
    Returns "Error" if air_quality_index is negative.
    Use: pollution = pollution_ranking(air_quality_index)
    -------------------------------------------------------
    Parameters:
        air_quality_index - Air Quality Index (int)
    Returns:
        pollution - name of pollution level (str)
    ------------------------------------------------------
    """
    if air_quality_index >= 0 and air_quality_index <= 50:
        result = "Good"

    elif air_quality_index >= 51 and air_quality_index <= 100:
        result = "Moderate"

    elif air_quality_index >= 101 and air_quality_index <= 150:
        result = "Unhealthy for Sensitive Groups"

    elif air_quality_index >= 151 and air_quality_index <= 200:
        result = "Unhealthy"

    elif air_quality_index >= 201 and air_quality_index <= 300:
        result = "Very Unhealthy"

    elif air_quality_index > 300:
        result = "Hazardous"

    elif air_quality_index < 0:
        result = "Error"

    return result

# task 3


def largest_average(val1, val2, val3):
    """
    -------------------------------------------------------
    Returns the average of the two largest values of
    val1, val2, and val3.
    Use: average = largest_average(val1, val2, val3)
    -------------------------------------------------------
    Parameters:
        val1 - a number (float)
        val2 - a number (float)
        val3 - a number (float)
    Returns:
        average - the average of the two largest values of
            val1, val2, and val3 (float)
    ------------------------------------------------------
    """
    # 100
    # 50
    # 25
    # val1 and two are biggest
    if val1 >= val2 and val1 >= val3:
        largest = val1
        second_largest = max(val2, val3)
    elif val2 >= val1 and val2 >= val3:
        largest = val2
        second_largest = max(val1, val3)
    else:
        largest = val3
        second_largest = max(val1, val2)

    # Calculate the average of the two largest values
    average = (largest + second_largest) / 2

    return average


# task 4
def colour_combine(rgb_colour1, rgb_colour2):
    """
    -------------------------------------------------------
    Determines the secondary rgb_colour from mixing two primary
    RGB (Red, Green, Blue) colours. The order of the colours
    is *not* significant.
    Returns "Error" if any of the rgb_colour parameter(s) are invalid.
        "red" + "blue": "fuchsia"
        "red" + "green": "yellow"
        "green" + "blue": "aqua"
        "red" + "red": "red"
        "blue" + "blue": "blue"
        "green" + "green": "green"
    Use: rgb_colour = colour_combine(rgb_colour1, rgb_colour2)
    -------------------------------------------------------
    Parameters:
        rgb_colour1 - a primary RGB rgb_colour (str)
        rgb_colour2 - a primary RGB rgb_colour (str)
    Returns:
        rgb_colour - a secondary RGB rgb_colour (str)
    -------------------------------------------------------
    """
    if rgb_colour1 == "red" and rgb_colour2 == "blue":
        colour = "fuchsia"

    elif rgb_colour1 == "blue" and rgb_colour2 == "red":
        colour = "fuchsia"

    elif rgb_colour1 == "red" and rgb_colour2 == "green":
        colour = "yellow"
    elif rgb_colour1 == "green" and rgb_colour2 == "red":
        colour = "yellow"

    elif rgb_colour1 == "green" and rgb_colour2 == "blue":
        colour = "aqua"

    elif rgb_colour1 == "blue" and rgb_colour2 == "green":
        colour = "aqua"

    elif rgb_colour1 == "red" and rgb_colour2 == "red":
        colour = "red"

    elif rgb_colour1 == "blue" and rgb_colour2 == "blue":
        colour = "blue"

    elif rgb_colour1 == "green" and rgb_colour2 == "green":
        colour = "green"

    else:
        colour = "Error"

    return colour


# task 5

def hoo_rah(number):

    if number % 2 == 0 and number % 7 == 0:
        result = "Hoo Rah"

    elif number % 2 == 0:
        result = "Hoo"

    elif number % 7 == 0:
        result = "Rah"

    else:
        result = "Zip"

    return result
