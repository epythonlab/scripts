
'''
    Problem: Longest Increasing Subsequence

    Write a Python function that takes a list of integers as input and returns
    the length of the longest increasing subsequence. 
    
    An increasing subsequence is a sequence of numbers in the list 
    that are in strictly increasing order (not necessarily contiguous). 

    For example, in the list [10, 22, 9, 33, 21, 50, 41, 60, 80], 

    the longest increasing subsequence is [10, 22, 33, 50, 60, 80], 
    so the function should return 6.
'''
longest_subsequence = [10, 22, 9, 33, 21, 50, 41, 60, 80]

current_subsequence = []
for i in range(0, len(longest_subsequence)):
    
    if i == 0 or longest_subsequence[i] > longest_subsequence[i-1]:
        current_subsequence.append(longest_subsequence[i])

print(current_subsequence)
print(len(current_subsequence))