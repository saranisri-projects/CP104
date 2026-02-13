"""
-------------------------------------------------------
Assignment 2, Task 1
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-28"
-------------------------------------------------------
"""
# getting user input
sales = int(input("Enter the total sales: $"))

# defining constant
TAX = 18.50

# formula
FINAL = sales*(TAX/100)

# final output with formatting
print()
print("Projected Tax Report")
print("--------------------")
print(f"Total sales: ${sales:.2f}")
print(f"Annual tax: %{TAX}")
print(f"Tax: ${FINAL:.2f}")
