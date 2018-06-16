import json
from urllib.request import urlopen

# Grab the 200 most recent TODOs
url = 'https://jsonplaceholder.typicode.com/todos'
json_obj = urlopen(url)

data = json.load(json_obj)

del data[-1]

for item in data:
	print ("TODO: " + str(item) )
# -----------------------------------

# Create a TODO

del data[::-1]



