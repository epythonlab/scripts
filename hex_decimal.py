"""
Python Challenge:
	Converting Hexadecimal to Decimal
"""
def hex_to_decimal(hex):

	return int(hex, 16)

# test the function

hex = 'A1F'
decimal = hex_to_decimal(hex)
print(decimal) # 2591