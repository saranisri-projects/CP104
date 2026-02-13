"""
-------------------------------------------------------
Lab 10, Task 6
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-21"
-------------------------------------------------------
"""
from functions import number_stats

nums = open('numbers.txt', 'r', encoding='utf-8')

print(number_stats(nums))

nums.close()
