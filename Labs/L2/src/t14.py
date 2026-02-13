"""
-------------------------------------------------------
Lab 2, Task 14
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# constants
MILK = 4
BUTTER = 8
FLOUR = 0.5
SALT = 2

# user input
servings = int(input("Enter servings of Mac & Cheese: "))

# base serving size
SERVING_SIZE = 6

# finding the multiple to multiply by based off 6
multiple = servings/SERVING_SIZE

# Calculate the required amounts using the constants
milk_needed = MILK * multiple
butter_needed = BUTTER * multiple
flour_needed = FLOUR * multiple
salt_needed = SALT * multiple

# Print the results
print()
print(servings, "servings of Mac & Cheese requires:")
print("milk (cups):", milk_needed)
print("butter (tablespoons):", butter_needed)
print("flour (cups):", flour_needed)
print("salt (teaspoons):", salt_needed)
