"""
-------------------------------------------------------
Lab 3, Task 4
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-27"
-------------------------------------------------------
"""
num = float(input("Enter number: "))
percent = float(input("Enter percent: "))

discount = percent/100
final = discount*num

print()
print(f"{percent:.1f} percent discount on {num:.1f} is {final:.1f}")

# A 10.5 percent discount on 500.0 is xx.x
