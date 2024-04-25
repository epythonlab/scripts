# zip() is used
# to iterate over multiple
# lists in parallel

nums = [1, 2, 3]
letters = ['a', 'b', 'c']

for char, num in zip(letters, nums):
    print(f'{char}:{num}')
