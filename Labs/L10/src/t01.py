"""
-------------------------------------------------------
Lab 10, Task 1
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-11-21"
-------------------------------------------------------
"""
from functions import customer_record

fh = open("customers.txt", "r")

print(customer_record(fh, 3))
print(customer_record(fh, 2))
print(customer_record(fh, 1))

fh.close()
