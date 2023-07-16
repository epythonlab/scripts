"""
how to check if file exists
in Python
"""
import os
def is_file_exists(file_path):
	return os.path.exists(file_path)

# test the function
file_path = 'main.py'
if is_file_exists(file_path):
	print('The file exists.')
else:
	print('The file does not exist')

