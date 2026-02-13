"""
-------------------------------------------------------
Lab 11, Task 3
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-29"
-------------------------------------------------------
"""
from functions import generate_matrix_num
from functions import print_matrix_num

matrix = generate_matrix_num(2, 5, -16, 10, "float")
print_matrix_num(matrix, 'float')

matrix = generate_matrix_num(2, 7, -16, 30, "float")
print_matrix_num(matrix, 'float')

matrix = generate_matrix_num(1, 7, -36, 10, "float")
print_matrix_num(matrix, 'float')
