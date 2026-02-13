"""
-------------------------------------------------------
Lab 2, Task 2
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# freezing constant
FREEZING = 32

# getting user input
farenheit = int(input("Temperature (F):"))
# formula for conversion
celsius = (farenheit-FREEZING)*(5/9)
# finding the decimal value
decimal = int((celsius * 10) % 10)

# if there is no decimal value, don't print

if decimal == 0:
    print("Temperature (C):", round(celsius))
# printing with decimal value
else:
    print("Temperature (C):", celsius)
