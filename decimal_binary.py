"""Python Challenge:
  Converts a Decimal number to binary
"""
def decimal2binary(decimal_number):
    """
    Converts a decimal number to binary 
    using the division method.

    Args:
        decimal_number: The decimal number to convert.

    Returns:
        The binary representation of the decimal number.
    """
    binary_repr = []
    quotient = decimal_number
    while quotient > 0:
        remainder = quotient % 2
        binary_repr.append(remainder)
        quotient = quotient // 2
    
    binary_repr.reverse()
    
    return binary_repr
  
# testing the code
decimal_number = 75
# [1, 0, 0, 1, 0, 1, 1]
binary_repr = decimal2binary(decimal_number)
print(binary_repr)

