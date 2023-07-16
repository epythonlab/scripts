"""Python Challenge: 
    String Encoding and Decoding
"""
import base64

def encoding(string):
    
    encoded = base64.b64encode(string.encode('utf-8'))
    
    return encoded

def decoding(byte):
    decoded = base64.b64decode(byte).decode('utf-8')
    return decoded

# test the function
string = 'epythonlab'
encoded = encoding(string)
print(f'Original string: {string}')
print(f'Encoded: {encoded}')

decoded = decoding(encoded)
print(f'After decoded: {decoded}')
