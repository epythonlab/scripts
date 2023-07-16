"""
 Phone number country and location tracing
 in Python with phonenumbers library
"""
# pip install phonenumbers

import phonenumbers
from phonenumbers import geocoder, carrier

def trace_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, None)
        country = geocoder.country_name_for_number(parsed_number, 'en')
        location = geocoder.description_for_number(parsed_number, 'en')
        subscriber_name = carrier.safe_display_name(parsed_number, 'en')
        
        return country, location, subscriber_name
    
    except phonenumbers.phonenumberutil.NumberParseException:
        return None, None

# testing the code
phone_number = "+14155534673"
country, location, subscriber_name = trace_phone_number(phone_number)

if country and location:
    print('Country:', country)
    print('Location:', location)
    print('Service provider:', subscriber_name)
else:
    print("Unable to trace the phone number.")
        
print(dir(carrier))
