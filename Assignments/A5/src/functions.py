"""
-------------------------------------------------------
Assignment 5, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-10-27"
-------------------------------------------------------
"""
# task 1


def calc_factorial(number):
    """
    -------------------------------------------------------
    Calculates and returns the factorial of number.
    Use: product = calc_factorial(number)
    -------------------------------------------------------
    Parameters:
        number - number to factorial (int > 0)
    Returns:
        product - number! (int)
    ------------------------------------------------------
    """

    product = 1

    for i in range(1, number+1):
        product = product*i

    return product

# task 2


def calories_treadmill(per_min, minutes):
    """
    Running on a treadmill burns a certain number of calories. calories_treadmill prints a table of the number of calories burned every five minutes given the number of calories burned per minute (per_min) an the total number of minutes run (minutes). Align the results and print with 1 decimal accuracy for the calories burned as shown in the example execution.

Provide the function docstring (documentation) following the CP104 style.

The function must use a for loop.

The function does not ask for input.
"""
    for i in range(5, minutes+1, 5):
        total = per_min*i

        print(f"{i:2}  {total:.1f}")
    return

# task 3


def arrow_up(rows):
    """
    -------------------------------------------------------
    Prints an upward-pointing arrow pattern of '#' characters.
    Use: arrow_up(rows)
    -------------------------------------------------------
    Parameters:
        rows - the number of rows in the arrow (int > 0)
    Returns:
        None
    ------------------------------------------------------
    """
    for i in range(rows):
        spaces_before = ' ' * (rows - i - 1)
        if i == 0:
            # Print only one '#' at the top of the arrow
            print(f"{spaces_before}#")
        else:
            # Print two '#' characters with spaces in between
            spaces_middle = ' ' * (2 * i - 1)
            print(f"{spaces_before}#{spaces_middle}#")
    return

# task 4


def multiplication_table(start_num, stop_num):
    """
    -------------------------------------------------------
    Prints a multiplication table for values from start_num to stop_num.
    Use: multiplication_table(start_num, stop_num)
    -------------------------------------------------------
    Parameters:
        start_num - the range start value (int)
        stop_num - the range stop value (int)
    Returns:
        None
    ------------------------------------------------------
    """

    print("   ", end="")
    for num in range(start_num, stop_num + 1):
        print(f"{num:4}", end="")
    print("\n" + "-" * (4 * (stop_num - start_num + 2)))

    for i in range(start_num, stop_num + 1):
        print(f"{i:2} |", end="")
        for j in range(start_num, stop_num + 1):
            print(f"{i * j:4}", end="")
        print()
    return

# task 5


def range_addition(start, increment, count):
    """
    -------------------------------------------------------
    Uses a for loop to sum values from start by increment.
    Use: total = range_addition(start, increment, count)
    -------------------------------------------------------
    Parameters:
        start - the range start value (int)
        increment - the range increment (int)
        count - the number of values in the range (int)
    Returns:
        total - the sum of the range (int)
    ------------------------------------------------------
    """
    total = 0
    for i in range(count):
        total += start + i * increment
    return total
