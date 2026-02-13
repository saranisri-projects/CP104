"""
-------------------------------------------------------
Assignment 3, Task 3
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-28"
-------------------------------------------------------
"""
# getting user input
num = int(input("Enter a date in the format YYMMDD: "))

# extracting each digit
year = num//10000
day = num % 100
month = num//100
month = month % 100

# printing in final form
print()
print(f"The reformatted date: {year}/{month}/{day}")
