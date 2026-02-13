"""
-------------------------------------------------------
Assignment 2, Task 5
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-28"
-------------------------------------------------------
"""
# user inputs
flength = float(input("Foundation length: (m): "))
fwidth = float(input("Foundation width: (m): "))
fheight = float(input("Foundation height: (m): "))
wall = float(input("Wall height (m): "))
concrete = float(input("Cost of concrete ($/m^3): "))
bricks = float(input("Cost of bricks ($/m^2): "))

# concrete
concrete_needed = flength*fwidth*fheight
cost_concrete = concrete_needed*concrete

# wall
side1 = wall*fwidth
side2 = wall*flength
total = (side1+side2)*2
cost_bricks = total*bricks

# total cost
total_cost = cost_concrete+cost_bricks
total_cost = f"{total_cost:,.2f}"

# final prints
print()
print(f"Concrete needed for foundation (m^3): {concrete_needed:.2f}")
print(f"Cost of concrete: ${cost_concrete:.2f}")
print(f"Bricks needed for walls (m^2): {total:.2f}")
print(f"Cost of bricks: ${cost_bricks:.2f}")
print(f"Total cost: ${total_cost}")
