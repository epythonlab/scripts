import cv2
import pytesseract
from PIL import Image

# Path to the Tesseract executable in Google Colab
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# Load the image from the specified path
image_path = 'math.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding to preprocess the image
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Perform OCR on the preprocessed image
custom_config = r'--oem 3'  # Customize configuration as needed
text = pytesseract.image_to_string(thresh, config=custom_config)

# Print the extracted text
print("Extracted text:", text)
