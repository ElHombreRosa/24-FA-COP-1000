"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
# Charge for this sign.
charge = 0.00
# Number of characters.
numChars = int(input("Enter the number of characters for the sign: "))
# Type of wood.
woodType = input("Enter the type of wood used for the sign (pine or oak): ")
# Color of characters.
color = input("Enter the color of the characters (black, white, or gold): ")
# Write assignment and if statements here as appropriate.
charge = 35.00

if numChars > 5: 
    charge += (numChars - 5) * 4.00

if woodType == "oak":
    charge += 20.00

if color == "gold":
    charge += 15.00
    

# Output Charge for this sign.
print("The charge for this sign is $" + str(format(charge, ".2f")))