"""
 "Python Challenge: 
 	Extract Even Numbers from a List
"""
def extract_even(numbers):
	# your code here
	even_numbers = []
	for num in numbers:
		if num % 2 == 0:
			even_numbers.append(num)
	return even_numbers

nums = range(2, 20)
print(extract_even(nums))  
# [2, 4, 6, 8, 10, 12, 14, 16, 18]

nums = range(2, 50, 5)
print(extract_even(nums))  
# [2, 12, 22, 32, 42]

