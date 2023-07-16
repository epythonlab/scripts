"""
Python Challenge:
	Binary number to List
"""
def binaryList(binary):
	binary_list = []

	for i in list(str(binary)):
		binary_list.append(int(i))
	return binary_list

# test the function
binary = int(input('Enter binary number:'))
# input: 10011
binary_list = binaryList(binary)
print(binary_list)
# output: [1, 0, 0, 1, 1]

