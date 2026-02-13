"""
-------------------------------------------------------
Lab 4, Functions    
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# imports
import math
from math import pi

# constants

# task 3


def area(radius):
    """
    -------------------------------------------------------
    Calculates and returns area of a circle.
    Use: ar = area(radius)
    -------------------------------------------------------
    Parameters:
        radius - radius of a circle (float >= 0)
    Returns:
        ar - area of a circle (float)
    ------------------------------------------------------
    """
    ar = pi*(radius**2)
    return ar

# task 6


def pythag(s1, s2):
    """
    -------------------------------------------------------
    Calculates and returns the radius, diameter, circumference,
    and area of circle defined by a right triangle.
    Use: radius, diam, circ, area = pythag(s1, s2)
    -------------------------------------------------------
    Parameters:
        s1 - length of side 1 of a right triangle (float > 0)
        s2 - length of side 2 of a right triangle (float > 0)
    Returns:
        radius - radius of the resulting circle (float)
        diam - diameter of the resulting circle (float)
        circ - circumference of the resulting circle (float)
        area - area of the resulting circle (float)
    ------------------------------------------------------
    """
    # hypotenuse
    c = math.sqrt((s1**2) + (s2**2))

    # radius, diameter, and area
    radius = c
    diameter = 2*c
    circumference = 2 * math.pi * radius
    area = math.pi * (radius ** 2)

    return radius, diameter, circumference, area

# task 7


def total_change(nickels, dimes, quarters, loonies, toonies):
    """
    -------------------------------------------------------
    Calculates the total value of a set of coins in dollars.
    Each coin is worth:
        nickel:  $0.05
        dime:    $0.10
        quarter: $0.25
        loonie:  $1.00
        toonie:  $2.00
    Use: total = total_change(nickels, dimes, quarters,
        loonies, toonies)
    -------------------------------------------------------
    Parameters:
        nickels - number of nickels (int >= 0)
        dimes - number of dimes (int >= 0)
        quarters - number of quarters (int >= 0)
        loonies - number of loonies (int >= 0)
        toonies - number of toonies (int >= 0)
    Returns:
        total - total value of coins (float)
    -------------------------------------------------------
    """
    T_NICKEL = nickels*0.05
    T_DIME = dimes*0.10
    T_QUARTER = quarters*0.25
    T_LOONIE = loonies*1.00
    T_TOONIE = toonies*2.00

    TOTAL = T_NICKEL+T_DIME+T_QUARTER+T_LOONIE+T_TOONIE

    return TOTAL

# task 11


def slope(x1, y1, x2, y2):
    """
    -------------------------------------------------------
    Calculates the slope of a line. Slope is calculated as
    rise / run, where rise is distance between y coordinates,
    and run is distance between x coordinates.
    Use: slp = slope(x1, y1, x2, y2)
    -------------------------------------------------------
    Parameters:
        x1 - x coordinate of first point on a graph (float)
        y1 - y coordinate of first point on a graph (float)
        x2 - x coordinate of second point on a graph (float)
        y2 - y coordinate of second point on a graph (float)
        x2 != x1
    Returns:
        slp - slope of the line through (x1,y1) and (x2,y2)
    -------------------------------------------------------
    """
    #rise and run
    rise = y2-y1
    run = x2-x1

    # slope
    slopeF = rise/run

    return slopeF
# task 13


def f_to_c(fahrenheit):
    """
    -------------------------------------------------------
    Converts temperatures in fahrenheit to celsius.
    Use: celsius = f_to_c(fahrenheit)
    -------------------------------------------------------
    Parameters:
        fahrenheit - temperature in fahrenheit (int >= -459)
    Returns:
        celsius - equivalent to celsius (float)
    -------------------------------------------------------
    """
    c = (fahrenheit-32)*5/9

    return c
