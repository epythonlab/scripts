# a function to check 
# a string is_palindrome

def is_palindrome(string):
	reversed_string = string[::-1]

	return reversed_string == string


# test code
# this code will return true,
# if it is palindrome, and false otherwise
string = 'racecar'

if is_palindrome(string):
	print('The string is palindrome!')
else:
	print('The string is not a palindrome!')


