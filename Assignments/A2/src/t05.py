"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# getting user input
principle = float(input("Principle: $"))
interest = float(input("Interest (%):"))
years = int(input("Number of years:"))
times = int(input("Number of times interest compounded per year:"))

# dividing
interest = interest/100

# formula
balance = principle*(1+interest/times)**(times*years)

print()
print("Balance: $", balance)
