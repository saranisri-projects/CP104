"""
-------------------------------------------------------
Assignment 3, Task 4
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-28"
-------------------------------------------------------
"""
flyers = int(input("Number of flyers: "))
people = int(input("Number of delivery people: "))

person = flyers//people
left = flyers - (person*people)

print()
print("Flyers per delivery person:", person)
print("Flyers left over:", left)
