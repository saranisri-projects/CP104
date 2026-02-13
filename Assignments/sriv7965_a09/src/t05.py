"""
-------------------------------------------------------
Assignment 9, Task 5
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
from functions import student_stats

with open("students.txt", "r") as wordFile:
    l_id, h_id, avg = student_stats(wordFile)

print(f"Lowest ID: {l_id}\nHighest ID: {h_id}\nAverage Mark: {avg}")
