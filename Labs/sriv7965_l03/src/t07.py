"""
-------------------------------------------------------
Lab 3, Task 7
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-10-26"
-------------------------------------------------------
"""
breakfast = float(input("Enter cost of breakfast: $"))
lunch = float(input("Enter cost of lunch: $"))
supper = float(input("Enter cost of supper: $"))

total = breakfast+lunch+supper
total = '%.2f' % total


breakfast = '%.2f' % breakfast
lunch = '%.2f' % lunch
supper = '%.2f' % supper


print()

print(f"{'Meal':<12}{'Cost':^10}")
print(f"{'Breakfast':<12}${breakfast:>8}")
print(f"{'Lunch':<12}${lunch:>8}")
print(f"{'Supper':<12}${supper:>8}")
print(f"{'Total':<12}${total:>8}")
