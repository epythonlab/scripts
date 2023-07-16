"""
Python Challenge:
	Convert binary to decimal
"""
def binary_to_decimal(binary):
	return int(binary, 2)
"""
def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
        decimal += (binary % 10) * (2 ** power)
        binary //= 10
        power += 1
    return decimal
"""

# test the function
binary = '11'
decimal = binary_to_decimal(binary)
print(decimal) # output: 3


