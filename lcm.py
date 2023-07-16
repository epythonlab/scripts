"""
 Find the least common multiples of two numbers
"""
import math
def lcm(a, b):
	""" Returns the least common multiples of a and b
	Args:
		a: the first number
		b: the second number
	Returns:
		the least common of
		a and b
	"""
	gcd = math.gcd(a, b)
	return a * b // gcd

# test the code
if __name__ == '__main__':
	a = int(input('Enter first number:'))
	b = int(input('Enter the second number:'))
	lcm = lcm(a, b)
	print(f'The lcm of {a} and {b} is {lcm}')
