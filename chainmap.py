# Combine multiple Dictionaries
from collections import ChainMap

# Define the dicts
default_config = {
    'debug': False,
    'logging': 'low'
}
user_config = {
    'logging': 'high'
}
combine = ChainMap(
    user_config,
    default_config
)
print(combine)


