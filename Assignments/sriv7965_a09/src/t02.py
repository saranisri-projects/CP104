"""
-------------------------------------------------------
Assignment 9, Task 2
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
from functions import read_integers

with open("numbers.txt", "r") as wordFile:
    result = read_integers(wordFile)
print(result)
