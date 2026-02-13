"""
-------------------------------------------------------
Assignment 8, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-10"
-------------------------------------------------------
"""

# task 1


def list_factors(number):
    """
    -------------------------------------------------------
    Function takes number and outputs lists of factors not including number itself
    -------------------------------------------------------
    Parameters:
        number - A positive integer (> 0).
    Returns:
        factors - A list of factors of the number excluding the number itself.
    -------------------------------------------------------
    """
    factors = []

    for i in range(1, number+1):
        if number % i == 0:
            if i != number:
                factors.append(i)

    return factors

# task 2


def list_positives():
    """
    -------------------------------------------------------
    Gets a list of positive numbers from a user.
    Negative numbers are ignored. Enter 0 to stop entries.
    Use: number_list = list_positives()
    -------------------------------------------------------
    Returns:
        number_list - A list of positive integers (list of int)
    ------------------------------------------------------
    """
    positive = []

    while True:
        try:
            num = int(input("Enter a positive number: "))

            if num == 0:
                break

            if num > 0:
                positive.append(num)

        except ValueError:
            print("Invalid.")

    return positive


# task 3
def get_indexes(numbers, target_number):
    """
    -------------------------------------------------------
    Finds the indexes of target_number in numbers.
    Use: index_list = get_indexes(numbers, target_number)
    -------------------------------------------------------
    Parameters:
        numbers - list of values (list)
        target_number - value to look for in num_list (*)
    Returns:
        index_list - list of indexes of target_number (list of int)
    -------------------------------------------------------
    """

    place = []

    for i in range(0, len(numbers)):

        if numbers[i] == target_number:
            place.append(i)

    return place

# task 4


def list_subtract(minuend, subtrahend):
    """
    -------------------------------------------------------
    Alters the contents of minuend so that it does not contain
    any values in subtrahend.
    i.e. the values in the first list that appear in the second list
    are removed from the first list.
    Use: list_subtract(minuend, subtrahend)
    -------------------------------------------------------
    Parameters:
        minuend - a list of values (list)
        subtrahend - a list of values to not include in difference (list)
    Returns:
        None
    ------------------------------------------------------
    """

    for i in minuend[:]:

        if i in subtrahend:
            minuend.remove(i)

    return


# task 5
def verify_sorted(numbers):
    """
    -------------------------------------------------------
    Determines whether a list is sorted.
    Use: in_order, index = verify_sorted(numbers)
    -------------------------------------------------------
    Parameters:
        numbers - a list of numbers (list)
    Returns:
        in_order - True if numbers is sorted, False otherwise (bool)
        index - index of first value not in order,
            -1 if in_order is True (int)
    ------------------------------------------------------
    """
    test = (numbers == sorted(numbers))
    if test == True:
        num = 1
    elif test == False:
        num = -1

    return test, num
