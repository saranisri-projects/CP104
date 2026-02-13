"""
-------------------------------------------------------
Lab 7, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-01"
-------------------------------------------------------
"""
# task 1
from random import randint


def hi_lo_game(high):
    """
    -------------------------------------------------------
    Plays a random higher-lower guessing game.
    Use: count = hi_lo_game(high)
    -------------------------------------------------------
    Parameters:
        high - maximum random value (int > 1)
    Returns:
        count - the number of guesses the user made (int)
    -------------------------------------------------------
    """
    number = randint(1, high)
    count = 0
    guess = None

    while guess != number:
        guess = int(input("Enter a number:"))
        count += 1

        if guess < number:
            print("Too low, try again.")
        elif guess > number:
            print("Too high, try again.")
        else:
            print("Congratulations - good guess!")
            print("You made", count, "guesses.")

    return count

# task 2


def power_of_two(target):
    """
    -------------------------------------------------------
    Determines the nearest power of 2 greater than or equal to
    a given target.
    Use: power = power_of_two(target)
    -------------------------------------------------------
    Parameters:
        target - value to find nearest power of 2 (int >= 0)
    Returns:
        power - first power of 2 >= target (int)
    -------------------------------------------------------
    """
    power = 1

    while power < target:
        power *= 2

    return power

# task 4


def sum_squares(target):
    """
    -------------------------------------------------------
    Determines the sum of squares closest to, and greater than or
    equal to, a target value.
    Use: final = sum_squares(target)
    -------------------------------------------------------
    Parameters:
        target - target value (int >= 0)
    Returns:
        final - the final sum of squares >= target (int)
    -------------------------------------------------------
    """

    num = 0
    i = 1
    final = 0

    # Continue until the cumulative sum of squares is >= target
    while final < target:
        sum_of_squares = i ** 2
        final += sum_of_squares  # Add the square to the final sum
        num += sum_of_squares  # Keep a running total of squares
        i += 1  # Move to the next integer

    return final


# task 8


def budget(available):
    """
    -------------------------------------------------------
    Asks a user for a series of expenses in a month. Calculate the
    total expenses and determines whether the user is in "Surplus",
    "Deficit", or "Balanced" status.
    Use: expenses, balance, status = budget(available)
    -------------------------------------------------------
    Parameters:
        available - money currently available (float >= 0)
    Returns:
        expenses - total monthly expenses (float)
        balance - remaining balance (float)
        status - One of (str):
            "Surplus" if user budget is in surplus
            "Deficit" if user budget is in deficit
            "Balanced" if user budget is balanced
    ------------------------------------------------------
    """
    entered = float(input("Enter an expense (0 to quit): $"))
    expenses = entered
    while entered != 0:
        entered = float(input("Enter another expense (0 to quit): $"))
        expenses += entered

    balance = available - expenses

    if expenses > available:
        status = 'Deficit'
    elif expenses < available:
        status = 'Surplus'
    elif expenses == available:
        status = 'Balanced'

    return(expenses, balance, status)
# task 10


def employee_payroll():
    """
    -------------------------------------------------------
    Calculates and returns the weekly employee payroll for all employees
    in an organization. For each employee, ask the user for the employee ID
    number, the hourly wage rate, and the number of hours worked during a week.
    An employee number of zero indicates the end of user input.
    Each employee is paid 1.5 times their regular hourly rate for all hours
    over 40. A tax amount of 3.625 percent of gross salary is deducted.
    Use: total, average = employee_payroll()
    -------------------------------------------------------
    Returns:
        total - total net employee wages (i.e. after taxes) (float)
        average - average employee net wages (float)
    ------------------------------------------------------
    """

    total = 0
    avg = 0
    employees = 1

    OVERTIME = 40
    OVERTIME_RATE = 1.5
    TAX_RATE = 3.625 / 100

    while True:
        empid = int(input("Enter Employee ID: "))

        if empid == 0:
            break

        wage = float(input("Hourly wage rate: "))
        hours = int(input("Hours worked: "))

        salary = wage * hours
        if hours > 40:
            salary = wage * OVERTIME + wage * \
                (hours - OVERTIME) * OVERTIME_RATE

        salary -= salary * TAX_RATE
        print(f"Net payment for employee {empid}: ${salary:.2f}")
        print()
        total += salary
        avg = total / employees
        employees += 1

    return(total, avg)
