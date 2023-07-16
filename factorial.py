"""
Python Challenge:
	Efficient Factorial Calculation 
	in Python: Optimizing Performance
"""
def factorial(n):
	if n == 0:
		return 1
	else:
		return n*factorial(n-1)

# test the function
fact = factorial(5)
print(fact) # 120