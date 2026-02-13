"""
-------------------------------------------------------
Lab 10, Task 10 
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
from functions import count_frequency_word


word = open('words.txt', 'r', encoding='utf-8')

print(count_frequency_word(word, "Python"))

word.close()
