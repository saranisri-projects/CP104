"""
-------------------------------------------------------
Assignment 9, Task 3
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
from functions import file_statistics

with open("addresses.txt", "r") as wordFile:
    ucount, lcount, dcount, wcount, rcount = file_statistics(wordFile)
    result_string = f"{ucount}, {lcount}, {dcount}, {wcount}, {rcount}"
    print(result_string)
