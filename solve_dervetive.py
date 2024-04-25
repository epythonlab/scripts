import pytesseract
from PIL import Image
import sympy as sp

# Load the image
img = Image.open('math.jpg')

# Use pytesseract to do OCR on the image
text = pytesseract.image_to_string(img)

# Print the extracted text
print("Extracted Text:", text)

# Parse the extracted text into a format that can be understood by SymPy
parsed_expression = sp.sympify(text)

# Compute the derivative using SymPy
derivative = sp.diff(parsed_expression, 'x')

# Print the original expression and its derivative
print("Original Expression:", parsed_expression)
print("Derivative:", derivative)
