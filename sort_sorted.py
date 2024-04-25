# Difference between sort() and sorted()

# sorted(
original_list = [3, 2, 5, 1]

sorted_list  = sorted(original_list, reverse=True)
print(f'Original_list:{original_list}')

print(f'Sorted():{sorted_list}')

# sort()
print('----------sort() ---- ---')
list2 = [3, 4, 1, 2]
list2.sort(reverse=True)
print(f'{list2}')