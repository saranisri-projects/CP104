"""
-------------------------------------------------------
Assignment 6, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-03"
-------------------------------------------------------
"""
# task 1


def total_wins():
    """
    -------------------------------------------------------
    Takes a number of strings from the user representing the output of a game. Once all the strings have been entered,
    Use: numwins = total_wins()
    -------------------------------------------------------
    Parameters:
        winning_team = The team color that wins a given round (str)
    Returns:
        numPurp, numGold = The number of times 'purple' and 'gold' appear, respectively (int, int)
    ------------------------------------------------------
    """

    numPurp = 0
    numGold = 0

    while True:
        winning_team = input("Enter the winning team: ")

        if winning_team == 'purple':
            numPurp += 1

        elif winning_team == 'gold':
            numGold += 1

        elif winning_team == ' ' or winning_team == '':
            break

        else:
            pass

    return(numPurp, numGold)

# task 2


def detect_prime(number):
    """
    -------------------------------------------------------
    Determines if number is a prime number.
    Use: prime = detect_prime(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int > 1)
    Returns:
        prime - True if number is prime, False otherwise (bool)
    ------------------------------------------------------
    """

    num = 2
    prime = True

    while num < number:

        if number % num == 0:
            prime = False
            break

        num += 1
    return(prime)

# task 3


def interest_table(principal_amount, interest_rate, payment):
    """
    -------------------------------------------------------
    Prints a table of monthly interest and payments on a loan.
    Use: interest_table(principal_amount, interest_rate, payment)
    -------------------------------------------------------
    Parameters:
        principal_amount - original value of a loan (float > 0)
        interest_rate - yearly interest interest_rate as a % (float >= 0)
        payment - the monthly payment (float > 0)
    Returns:
        None
    ------------------------------------------------------
    """

    monthly_interest_rate = interest_rate / 12 / 100
    month = 0

    print(f"{'Month':<10}{'Interest':<15}{'Payment':<15}{'Remaining Balance':<20}")
    print("-" * 60)

    while principal_amount > 0:

        interest = principal_amount * monthly_interest_rate
        month += 1

        if principal_amount + interest < payment:
            payment = principal_amount + interest

        principal_amount = principal_amount + interest - payment

        print(f"{month:<10}{interest:<15.2f}{payment:<15.2f}{principal_amount:<20.2f}")

    return
# task 4


def count_of_digits(number):
    """
    -------------------------------------------------------
    Counts the number of digits in an integer.
    Use: digits = count_of_digits(number)
    -------------------------------------------------------
    Parameters:
        number - an integer (int)
    Returns:
        digits - the number of digits in number (int)
    ------------------------------------------------------
    """

    digits = 0

    if number < 0:
        number *= -1

    while number // 10 > 0:
        number = number // 10
        digits += 1

    digits += 1
    return(digits)

# task 5


def factor_summation(number):
    """
    -------------------------------------------------------
    Determines the sum of factors of an integer not including
    the integer itself. An integer's factors are the whole numbers
    that the integer can be evenly divided by.
    Use: total = factor_summation(number)
    -------------------------------------------------------
    Parameters:
        number - a positive integer (int >= 1)
    Returns:
        total - the total of number's factors (int)
    ------------------------------------------------------
    """

    factor = 1
    total = 0
    while factor < number:
        if number % factor == 0:
            total += factor
        else:
            pass
        factor += 1

    return(total)
