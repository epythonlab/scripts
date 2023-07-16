import re
CommonPrefixes = {'Prefix': 'JG/BMF/'}

result = re.split(r'/', CommonPrefixes['Prefix'])

print(result)