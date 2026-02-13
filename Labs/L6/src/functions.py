"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-10-25"
-------------------------------------------------------
"""
# task 3


def sum_all(start, finish, increment):
    """
    -------------------------------------------------------
    Sums and returns all numbers from start to finish (inclusive)
    by increment.
    Use: total = sum_all(start, finish, increment)
    -------------------------------------------------------
    Parameters:
        start - an integer (int > 0)
        finish - an integer (int >= start)
        increment - an integer (int > 0)
    Returns:
        total - sum of all numbers from start to
            finish by increment (int)
    ------------------------------------------------------
    """
    total = 0

    for num in range(start, finish+1, increment):
        total += num
    return total


# task 8
def draw_hollow_triangle(width, char):
    """
    -------------------------------------------------------
    Prints a hollow triangle of width characters using
    the char character.
    Use: draw_hollow_triangle(width, char)
    -------------------------------------------------------
    Parameters:
        width - number of characters wide (int > 0)
        char - the character to draw with (str, len() == 1)
    Returns:
        None
    ------------------------------------------------------
    """

    for row in range(width):
        for col in range(width):
            if col == 0 or row == (width-1) or row == col:
                # stars
                print(char, end="")
            else:
                print(end=" ")
        print()


# task 11


def retirement(age, salary, increase):
    """
    -------------------------------------------------------
    Calculates and prints a table of how much a worker earns
    between age and retirement at 65.
    Use: retirement(age, salary, increase)
    -------------------------------------------------------
    Parameters:
        age - worker's current age (int > 0)
        salary - worker's current salary (float > 0)
        increase - percent increase in salary per year (float >= 0)
    Returns:
        None
    ------------------------------------------------------
    """
    rate = 1+increase/100
    print("Age         Salary")
    print("------------------")
    retirment = 65
    for i in range(age, retirment+1):
        print(f"{i:2d}{salary:16,.2f}")
        salary *= rate
    return

# task 13


def lumber(b_min, b_max, b_inc, h_min, h_max, h_inc):
    """
    -------------------------------------------------------
    Create a table of the engineering properties of lumber.
    Given the base and height of a piece of lumber in inches,
    different properties of a piece of lumber are calculated as:
        cross-sectional area = base × height
        moment of inertia = base × height^3 / 12
        section modulus = base × height^2 / 6
    Use: lumber(b_min, b_max, b_inc, h_min, h_max, h_inc)
    -------------------------------------------------------
    Parameters:
        b_min - minimum value of base (int > 0)
        b_max - maximum value of base (int > b_min)
        b_inc - increment in base value (int > 0)
        h_min - minimum value of height (int > 0)
        h_max - maximum value of height (int > h_min)
        h_inc - increment in height value (int > 0)
    Returns:
        None
    -------------------------------------------------------
    """
    print(f"{'Cross-Sectional':>35}{'Moment of  Section':>20}")
    print(f"{'Base':>3}  {'Height':>3}  {'Cross-Sectional Area':>20}  {'Moment of Inertia':>15}  {'Section Modulus':>10}")
    print('-' * 70)

    for base in range(b_min, b_max + 1, b_inc):
        for height in range(h_min, h_max + 1, h_inc):
            area = base * height
            moment_of_inertia = (base * (height ** 3)) / 12
            section_modulus = (base * (height ** 2)) / 6
            print(
                f"{base:>3}  x {height:<3}  {area:>20,.2f}  {moment_of_inertia:>15,.2f}  {section_modulus:>10,.2f}")

    return


# task 14
def ia_hours(ia_count):
    """
    -------------------------------------------------------
    Calculates the total number of hours that IAs (Instructional
    Assistants) work over a 6 week period by asking for the hours
    for each IA per week.
    Use: total_hours = ia_hours(ia_count)
    -------------------------------------------------------
    Parameters:
        ia_count - number of IAs (int > 0)
    Returns:
        total_hours - hours worked by all IAs (float)
    ------------------------------------------------------
    """
    NUM_WEEKS = 6
    total_hours = 0.0

    for week in range(1, NUM_WEEKS + 1):
        print(f"Week {week}")

        # For each week, ask for hours for each IA
        for i in range(1, ia_count + 1):
            # Prompt user for IA's hours
            hours = float(input(f"  Marking hours for IA {i}: "))
            total_hours += hours  # Add hours to the total

    # Print and return the total hours worked over 6 weeks
    print(f"\n{total_hours:.2f}")
    return total_hours
