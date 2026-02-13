"""
-------------------------------------------------------
Assignment 9, Task 1
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
from functions import file_top

with open("students.txt", "r") as wordFile:
    file_top(wordFile, 5)
