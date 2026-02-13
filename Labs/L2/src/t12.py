"""
-------------------------------------------------------
Lab 2, Task 12
-------------------------------------------------------
Author:  Sarani Srivijayasri
ID:      169087965
Email:   sriv7965@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""
# Constants for time conversions
SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = 3600
SECONDS_PER_DAY = 86400

# Get the number of seconds from the user
total_seconds = int(input("Number of seconds: "))

# Calculate days, hours, minutes, and seconds
days = total_seconds // SECONDS_PER_DAY
remaining_seconds = total_seconds % SECONDS_PER_DAY
hours = remaining_seconds // SECONDS_PER_HOUR
remaining_seconds %= SECONDS_PER_HOUR
minutes = remaining_seconds // SECONDS_PER_MINUTE
seconds = remaining_seconds % SECONDS_PER_MINUTE

# Print the results
print()
print("Days:", days, "Hours:", hours, "Minutes:", minutes, "Seconds:", seconds)
