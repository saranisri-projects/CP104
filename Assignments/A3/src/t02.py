"""
-------------------------------------------------------
Assignment 2, Task 2
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-28"
-------------------------------------------------------
"""
# getting user input
num = int(input("Enter a positive digit number: "))

# extracting digits
first = num//10
second = num % 10

# equation
difference = first-second

# final ouput
print()
print("The difference of the digits of", num, "is", difference)
