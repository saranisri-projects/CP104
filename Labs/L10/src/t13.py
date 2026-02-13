"""
-------------------------------------------------------
Lab 10, Task 13
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
from functions import file_copy

words = open("words.txt", "r")

newFile = open("newFile.txt", 'w')

file_copy(words, newFile)

words.close()
newFile.close()
