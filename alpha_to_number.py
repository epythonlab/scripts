""" Python Challenge:
       how to convert alphabets to 
       numbers using the A1Z26 cipher
"""
def alpha_to_numbers(alphabets):
    numbers = []
    
    for letter in alphabets.replace(' ', ''):
        number = ord(letter.upper()) - ord('A') + 1
        numbers.append(number)
    
    return numbers

# test the function
alphabets = 'epython lab'
# numbers = [5, 16, 25, 20, 8, 15, 14, 12, 1, 2]

print(alpha_to_numbers(alphabets))