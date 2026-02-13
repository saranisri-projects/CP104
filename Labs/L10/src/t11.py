"""
-------------------------------------------------------
Lab 10, Task 11
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
from functions import find_longest

word = open('words.txt', 'r', encoding='utf-8')

print(f"'{find_longest(word)}' is the last longest word")
