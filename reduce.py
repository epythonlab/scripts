# reduce() function
from functools import reduce
nums = [2, 3, 4, 5, 8, 9]

sum = reduce(lambda x,y: x+y, nums)
print(sum)
