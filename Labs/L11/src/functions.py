"""
-------------------------------------------------------
Lab 11, Functions
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-29"
-------------------------------------------------------
"""
import random

# task 1


def generate_matrix_num(rows, cols, low, high, value_type):
    """
    -------------------------------------------------------
    Generates a 2D list of numbers of the given type, 'float' or 'int'.
    (To generate random float number use random.uniform and to
    generate random integer number use random.randint)
    Use: matrix = generate_matrix_num(rows, cols, low, high, value_type)
    -------------------------------------------------------
    Parameters:
        rows - number of rows in the list (int > 0)
        cols - number of columns (int > 0)
        low - low value of range (float)
        high - high value of range (float > low)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        matrix - a 2D list of random numbers (2D list of float/int)
    -------------------------------------------------------
    """
    matrix = []

    for _ in range(rows):
        row = []
        for _ in range(cols):
            if value_type == 'float':
                row.append(random.uniform(low, high))
            elif value_type == 'int':
                row.append(random.randint(int(low), int(high)))
        matrix.append(row)

    return matrix


# task 3
def print_matrix_num(matrix, value_type):
    """
    -------------------------------------------------------
    Prints the contents of a 2D list in a formatted table.
    Prints float values with 2 decimal points and prints row and
    column headings.
    Use: print_matrix_num(matrix, 'float')
    Use: print_matrix_num(matrix, 'int')
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of values (2D list)
        value_type - type of values in the list, 'float' or 'int' (str)
    Returns:
        None.
    -------------------------------------------------------
    """
    print(f"{' ':>3}", end="")
    for col in range(len(matrix[0])):
        print(f"{col + 0:5}", end="")
    print()

    # Printing the rows
    for row_index, row in enumerate(matrix):
        print(f"{row_index + 0:2} ", end="")

        # Printing the values
        for value in row:
            if value_type == 'float':
                print(f"{value:5.2f}", end="")

            elif value_type == 'int':
                print(f"{value:5d}", end="")

            else:
                print(f"{0:5d}", end="")

        # Blank print for formatting
        print()

    return

# task 7


def find_position(matrix):
    """
    -------------------------------------------------------
    Determines the first locations [row, column] of smallest and
    largest values in a 2D list.
    Use: s_loc, l_loc = find_position(matrix)
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list of numbers (2D list)
    Returns:
        s_loc - a list of of the row and column location of
            the smallest value in matrix (list of int)
        l_loc - a list of of the row and column location of
            the largest value in matrix (list of int)
    -------------------------------------------------------
    """

    if not matrix:
        min_loc = [0, 0]
        max_loc = [0, 0]

    else:
        rows = len(matrix)
        cols = len(matrix[0])
        min_val = matrix[0][0]
        max_val = matrix[0][0]
        min_loc = [0, 0]
        max_loc = [0, 0]

        # Using for loops to look at each individual value
        for i in range(rows):
            for j in range(cols):

                # finding if the value is smaller
                if matrix[i][j] < min_val:
                    min_val = matrix[i][j]
                    min_loc = [i, j]

                # finding if the value is larger
                elif matrix[i][j] > max_val:
                    max_val = matrix[i][j]
                    max_loc = [i, j]

    return min_loc, max_loc

# task 13


def matrix_scalar_multiply(matrix, num):
    """
    -------------------------------------------------------
    Update matrix by multiplying each element of matrix by num.
    Use: matrix_scalar_multiply(matrix, num)
    -------------------------------------------------------
    Parameters:
        matrix - the matrix to multiply (2D list of int/float)
        num - the number to multiply by (int/float)
    Returns:
        None
    ------------------------------------------------------
    """
    if not matrix:
        num = num

    else:
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = matrix[i][j] * num

    return matrix


# task 14


def matrix_transpose(matrix):
    """
    -------------------------------------------------------
    Transpose the contents of matrix. (Swap the rows and columns.)
    Use: transposed = matrix_transpose(matrix):
    -------------------------------------------------------
    Parameters:
        matrix - a 2D list (2D list of *)
    Returns:
        transposed - the transposed matrix (2D list of *)
    ------------------------------------------------------
    """
    if not matrix:
        transposed = []

    else:
        rows = len(matrix)
        cols = len(matrix[0])
        transposed = [[None] * rows for k in range(cols)]

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

    return transposed
