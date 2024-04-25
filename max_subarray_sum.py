# Python challenge: Given an array of integers, 
# find the maximum possible sum of a subarray,
# where the subarray must contain at least one element.
# - This is a classic algorithmic problem that 
# can be solved with a dynamic programming approach.


def max_subarray_sum(nums):
    if not nums:
        return 0    # empty array
    
    max_sum = nums[0]
    current_sum = nums[0]
    
    for num in nums[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# test this function
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = max_subarray_sum(nums)
print(f'max subarray sum is: {result}')