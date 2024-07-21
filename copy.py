# Shallow vs Deep copy
from copy import copy, deepcopy

original_list = [1, 2, [3, 4]]

print(f'Original List before copied: {original_list}')

shallow_copied = copy(original_list)
shallow_copied[2][0] = 5 # Shallow

print(f'Original list after copied:{original_list}')
print(f'Shallow Copied List: {shallow_copied}')

deep_copied = deepcopy(original_list)
deep_copied[2][0] = 2 # Deep
print(f'Deep copied list: {deep_copied}')



