"""
Python Challenge:
	Convert Integer to times
"""
from datetime import datetime
# create list of integers
numbers = [930, 1215, 1500, 1850]
# convert to times
times = []
for num in numbers:
	num_str = str(num)
	time_ob = datetime.strptime(
		num_str, '%H%M')
	time_formatted = time_ob.strftime('%H:%M')
	times.append(time_formatted)

# print converted times
print(*times, sep='\n')


