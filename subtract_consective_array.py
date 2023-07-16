"""
Python Challege:
    Subtract Consecutive Array Elements
    
"""
# Let's we have an array
a = [1, 3, 4, 7, 9, 2]
# [1-3, 4-7, 9-2]
# the most efficient 
# solution is using zip()
res = [abs(x-y) for x,y in zip(a[::2], a[1::2])]
print(res)

# Output:  [2, 3, 7]

