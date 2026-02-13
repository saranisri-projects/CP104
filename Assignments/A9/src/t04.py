"""
-------------------------------------------------------
Assignment 9, Task 4
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
from functions import line_numbering

input_file = "wilde.txt"
output_file = "wilde_numbered.txt"

with open(input_file, "r") as wordFile:
    with open(output_file, "w") as outputFile:
        line_numbering(wordFile, outputFile)

print(f"The file {output_file} has been created with line numbers.")
