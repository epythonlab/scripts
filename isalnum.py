"""
Python Challenge:
	how to easily check if all 
	characters in the given 
	string is alphanumeric?
"""
def is_alphanumeric(string):
	"""Checks if all characters in 
	the given string are alphanumeric.

	Args:
		string: The string to check.

	Returns:
		True if all characters in the 
		string are alphanumeric, 
			False otherwise.
	"""
	# Method 1: isalnum()
	#return string.isalnum()

	# Method 2: using regular expression
	import re
	pattern = r'^[a-zA-Z0-9]+$'
	res = re.match(pattern, string)
	return bool(res)

# Example usage:
string1 = "Hello123"
print(is_alphanumeric(string1))  
# True

string2 = "Hello!123"
print(is_alphanumeric(string2)) 
 # False