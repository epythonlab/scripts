# Write a function how 
# to reverse a string
def reverse_string(string):
	""" Reverses a string
		Args:
			string: the string to be reversed
		Return:
			the reversed string
	"""
	reversed_string = ""
	for i in range(len(string) -1, -1, -1):
		reversed_string += string[i]
	return reversed_string

# test the function
string = "epython lab"
reversed_string = reverse_string(string)
print(f'Original string: {string}')
print(f'Reversed string: {reversed_string}')