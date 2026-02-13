"""
-------------------------------------------------------
Lab 5, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-10-11"
-------------------------------------------------------
"""
# task 1


def magic_date(day, month, year):
    """
    -------------------------------------------------------
    Determines if a date is magic. A date is magic if the day
    times the month equals the year.
    Use: magic = magic_date(day, month, year)
    -------------------------------------------------------
    Parameters:
        day - numeric day (int > 0)
        month - numeric month (int > 0)
        year - numeric two-digit year (int > 0)
    Returns:
        magic - True if date is magic, False otherwise (boolean)
    -------------------------------------------------------
    """
    return day*month == year

# task 6


def is_divisible(n, i, j):
    """
    -------------------------------------------------------
    Determines if n is evenly divisible by both i and j.
    Use: result = is_divisible(n, i, j)
    -------------------------------------------------------
    Parameters:
        n - the number to check for divisibility (int)
        i - one of the values to divide n by (int)
        j - another value to divide n by (int)
    Returns:
        result - True if n is evenly divisible by both
            i and j, False otherwise (boolean)
    ------------------------------------------------------
    """
    result = (n % i == 0) and (n % j == 0)

    return result
# task 9


def wind_speed(speed):
    """
    -------------------------------------------------------
    description
    Use: category = wind_speed(speed)
    -------------------------------------------------------
    Parameters:
        speed - wind speed in km/hr (int >= 0)
    Returns:
        category - description of wind speed (str)
    ------------------------------------------------------
    """

    if speed < 0:
        category = "Unknown"
    elif 0 <= speed < 39:
        category = "Breeze"
    elif 39 <= speed <= 61:
        category = "Strong Wind"
    elif 62 <= speed <= 88:
        category = "Gale Winds"
    elif 89 <= speed <= 117:
        category = "Whole Gale"
    else:
        category = "Hurricane"

    return category

# task 11


def quadrant(x, y):
    """
    -------------------------------------------------------
    Determines location on a plane of an x, y coordinate.
    Use: location = quadrant(x, y)
    -------------------------------------------------------
    Parameters:
        x - x coordinate on a Cartesian plane (float)
        y - y coordinate on a Cartesian plane (float)
    Returns:
        location - one of: 'Quadrant 1', 'Quadrant 2', 'Quadrant 3'
          'Quadrant 4', 'X-Axis', 'Y-Axis', 'Origin' (str)
    -------------------------------------------------------
    """
    if x == 0 and y == 0:
        location = "Origin"
    elif x == 0:
        location = "Y-Axis"
    elif y == 0:
        location = "X-Axis"
    elif x > 0 and y > 0:
        location = "Quadrant 1"
    elif x < 0 and y > 0:
        location = "Quadrant 2"
    elif x < 0 and y < 0:
        location = "Quadrant 3"
    else:
        location = "Quadrant 4"

    return location

# task 13


def loan():
    """
    -------------------------------------------------------
    An employee may qualify for a loan if they have worked for a
    minimum of 5 years, and has a salary of $30,000 or more.
    This function must ask for the years employed and the salary
    as appropriate.
    Use: qualified = loan()
    -------------------------------------------------------
    Returns:
        qualified - True if employee qualifies for a loan,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    # constants
    MIN_YEARS = 5
    MIN_SALARY = 30000

    year = int(input("Years employed: "))
    salary = int(input("Annual salary: "))
    print()

    QUALIFIED = False

    if year >= MIN_YEARS:
        if salary >= MIN_SALARY:
            QUALIFIED = True

    return QUALIFIED
