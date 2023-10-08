# How to validate phone number using regex
# in Python

import re

def is_phone_number_valid(phone_number):
    # define a regex pattern for a basic phone validation
    pattern = r'^(?:\+?\d{1,3}[-.])?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    
    # use re.match to check if the phone number maches the pattern
    if re.match(pattern, phone_number):
        return True
    else:
        return False

# test the function
# list of phone numbers
phone_numbers = ["+1 (123) 456-7890",
                 '555-5555',
                 '123.456.456 7890',
                 '+12-456.7890',
                 '+44 20 7946 0958',
                 '123-456-7890']

for phone in phone_numbers:
    is_valid = is_phone_number_valid(phone)
    print(f'{phone} is valid: {is_valid}')





