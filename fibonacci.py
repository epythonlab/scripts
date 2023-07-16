# Prints Fibonacci
# Sequence
def fib(n):
	if n == 0 or n == 1:
		return n
	else:
		return fib(n-1)+fib(n-2)

def main():
	n = int(input('Enter a number:'))
	print(f'Fibonacci sequence of {n} is:')

	for i in range(n):
		print(fib(i))

# test the code
if __name__ == '__main__':
	main()
