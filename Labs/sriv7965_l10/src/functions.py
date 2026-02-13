"""
-------------------------------------------------------
Lab 10, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-12-10"
-------------------------------------------------------
"""
# task 1


def customer_record(fh, n):
    """
    -------------------------------------------------------
    Find the n-th record in a comma-delimited sequential file.
    Records are numbered starting with 0.
    Use: result = customer_record(fh, n)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        n - the number of the record to return (int >= 0)
    Returns:
        result - a list of the fields of the n-th record if it exists,
            an empty list otherwise (list)
    -------------------------------------------------------
    """

    result = fh.readline().strip().split(",")

    count = 0

    while count != n:
        result = fh.readline().strip().split(",")
        count += 1

    if result == ['']:
        result = []

    return(result)


# task 6
def number_stats(fh):
    """
    -------------------------------------------------------
    Returns statistics on the numbers in a file.
    Assumes file is not empty.
    Use: smallest, largest, total, average = number_stats(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        smallest - smallest number (int)
        largest - largest number (int)
        total - sum of all the numbers in the file (int)
        average - average of all the numbers (float)
    ------------------------------------------------------
    """
    count = 1

    firstnum = int(fh.readline().strip())

    smallest = firstnum
    largest = firstnum
    total = firstnum

    for line in fh:
        if smallest > int(line.strip()):
            smallest = int(line.strip())
        elif largest < int(line.strip()):
            largest = int(line.strip())
        total += int(line.strip())
        count += 1

    average = total / count
    return(smallest, largest, total, average)

# task 10


def count_frequency_word(fh, word):
    """
    -------------------------------------------------------
    Counts the number of appearances of word in fh.
    Case is significant - line in file must match word in case.
    Use: count = count_frequency_word(fh, word)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
        word - the word to search for it in fh (str)
    Returns:
        count - the number of appearance of word in fh (int)
    ------------------------------------------------------
    """
    count = 0

    for line in fh:
        currword = line.strip()

        if currword == word:
            count += 1

    return(count)


# task 11


def find_longest(fh):
    """
    -------------------------------------------------------
    Finds the last word with longest length in fh.
    Assumes file is not empty.
    Use: word = find_longest(fh)
    -------------------------------------------------------
    Parameters:
        fh - file to search (file handle - already open for reading)
    Returns:
        word - the last word with the longest length in fh (str)
    ------------------------------------------------------
    """
    longest = ''

    for length in fh:

        words = length.strip().split()

        for word in words:
            # If the current word is longer or if it has the same length but appears later
            if len(word) >= len(longest):
                longest = word

    return longest


# task 13

def file_copy(fh_1, fh_2):
    """
    -------------------------------------------------------
    Copies the contents of fh_1 to fh_2.
    Any contents of fh_2 are overwritten.
    Use: file_copy(fh_1, fh_2)
    -------------------------------------------------------
    Parameters:
        fh_1 - source file (file handle - already open for reading)
        fh_2 - target file (file handle - already open for writing)
    Returns:
        None
    ------------------------------------------------------
    """
    for lines in fh_1:
        fh_2.write(lines)

    return
#


def has_city(travel_file, city_name):
    # City name not yet found.
    city_found = False
    # Get the first city in the file.
    city = travel_file.readline()

    while city != "" and city.strip() != city_name:
        # Get the next city in the file.
        city = travel_file.readline()

    # See why loop stopped - end of file or city names match?
    if city != "":
        # End of file not reached.
        city_found = True
    return city_found


filename = input("Enter the file name: ")
city_name = input("Enter the city name to look for: ")
travel_file = open(filename, "r", encoding="utf-8")
result = has_city(travel_file, city_name)
travel_file.close()
