# Shallow Copy of a Dictionary
original_dict = {'a': 1,
                 'b': {'x': 10}}
# 1. Shallow copy using 
# dictionary constructor(dict())
copied_dict = dict(original_dict)

# 3. Shallow copy using 
# copy() method
copied_dict = original_dict.copy()
# Modify the copied_dict
copied_dict['b']['x'] = 50

print("Original:", original_dict)
print("Copied:", copied_dict)

