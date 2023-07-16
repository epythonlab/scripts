"""
Read and parse yaml file
get list of table names from yaml file
"""
import yaml
def get_table_names(file_path):

	"""
	Returns list of table names from the yaml file

	Args:
		file_path : the path of the yaml file
	Returns:
		returns the list of table names

	"""
	with open(file_path, 'r') as file:
		data = yaml.load(file, Loader=yaml.FullLoader)
	return data

# test the function
file_path = '/home/noh/Downloads/Telegram Desktop/Retail.YAML'

result = get_table_names(file_path)
table_names = []
for k in result['databaseColumns']:
	if not k['tableName'] in table_names:
		table_names.append(k['tableName'])
print(table_names)

#print(result['DataElements'])
