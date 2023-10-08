# Deepcopy in python

import copy

list_1 = [1, 2, 3, 4]

# copy the original list
copied_list = copy.deepcopy(list_1)

# Modify the copied list
copied_list.append(10)

# modify the original list
list_1.append(5)

print(f'Original List: {list_1}')
print(f'Copied List: {copied_list}')

