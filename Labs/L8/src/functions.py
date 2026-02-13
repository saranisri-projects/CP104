"""
-------------------------------------------------------
Lab 8, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-06"
-------------------------------------------------------
"""
# task 3


def get_digit_name(n):
    """
    -------------------------------------------------------
    Returns the name of a digit given its number.
    Use: name = get_digit_name(n)
    -------------------------------------------------------
    Parameters:
        n - digit number (int 0 <= n <= 9)
    Returns:
        name - matching digit, 0 = "zero", 9 = "nine" (str)
    -------------------------------------------------------
    """
    NUMBERS = ["zero", "one", "two", "three", "four",
               "five", "six", "seven", "eight", "nine"]

    NUMBERS = NUMBERS[n]

    return NUMBERS

# task 6


def list_stats(values):
    """
    -------------------------------------------------------
    Returns statistics about values in a list.
    values has at least one element.
    Use: smallest, largest, total, average = list_stats(values)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of float)
    Returns:
        smallest - the smallest number in values (float)
        largest - the largest number in values (float)
        total - total of numbers in list (float)
        average - the average numbers in values (float)
    -------------------------------------------------------
    """
    values.sort()
    smallest = values[0]
    largest = values[-1]

    start = 0

    for n in values:
        start += n

    average = start/len(values)

    return smallest, largest, start, average


# task 9
def many_search(values, value):
    """
    -------------------------------------------------------
    Searches through values for value and returns a list of
    all indexes of its occurrence.
    User: indexes = many_search(values, value)
    -------------------------------------------------------
    Parameters:
        values - a list of values (list of *).
        value - can be compared to items in values (*).
    Returns:
        indexes - a list of indexes of the location of value in values,
            [] if not found (list of int).
    -------------------------------------------------------
    """

    size = len(values)
    index = []

    for itr in range(size):

        if (values[itr] == value):
            index.append(itr)

    return index

# task 12


def list_sums(source1, source2):
    """
    -------------------------------------------------------
    Calculates sums of elements of two lists. Lists must be the
    same length.
    Use: target = list_sums(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - list of numbers (list of float)
        source2 - list of numbers (list of float)
    Returns:
        target - sums of elements of source1 and source2 (list of float)
    -------------------------------------------------------
    """
    sums = []

    for n in range(0, len(source1)):
        sums.append(source1[n] + source2[n])

    return sums

# task 14


def intersection(source1, source2):
    """
    -------------------------------------------------------
    Returns a list that is the intersection of the contents of source1 and source2.
    Only elements that appear in both source1 and source2
    appear once and only once in target.
    Use: target = intersection(source1, source2)
    -------------------------------------------------------
    Parameters:
        source1 - a list (list of *)
        source2 - a list (list of *)
    Returns:
        target - the intersection of source1 and source2 (list of *)
    -------------------------------------------------------
    """

    set1 = set(source1)
    set2 = set(source2)

    # Find the intersection of both sets
    intersection_set = set1 & set2

    # Convert the intersection set back to a list
    target = list(intersection_set)

    return target
