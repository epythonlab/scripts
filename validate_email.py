# How to validate email using regex
# in Python

import re

def is_email_valid(email):
    # define a regex pattern for a basic email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    # use re.match to check if the email maches the pattern
    if re.match(pattern, email):
        return True 
    else:
        return False
    
 
# test the function
# list of emails
emails = ["example@gmail.com",
          'epython.com', 
          'epython@info.com',
          'ep-info.com',
          'ep-info@gmail.com']
for email in emails:
    is_valid = is_email_valid(email)
    print(f'{email} is valid: {is_valid}')

