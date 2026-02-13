"""
-------------------------------------------------------
Lab 2, Task 6
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-19"
-------------------------------------------------------
"""
# getting user input
mortgage = int(input("Mortgage principle ($): "))
years = int(input("Number of years: "))
interest = float(input("Yearly interest rate (%): "))
# how many months are in the years
months = years*12
# multiplying interest by 12 for months and dividing the percent
monthly = (interest/12)/100

# final formula
payment = (mortgage)*((monthly*(1+monthly)**months))/(((1+monthly)**months)-1)

# final print statement
print()
print("The monthly payments are: $", payment)
