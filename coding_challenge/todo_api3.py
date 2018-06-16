# importing the requests library
import requests
 
# grab TODOs from JSON placeholder
URL = 'https://jsonplaceholder.typicode.com/todos' 

# GET request
r = requests.get(url = URL)
 
# extracting data in json format
data = r.json()

# print TODOs
#for item in data:
	#print ("TODO: " + str(item) )
 

# print("string value: %s" % data[1]['id'])

# Delete TODO by ID, last element deleted
#del data[-1]


# Create TODO with new ID, last element replaced
#new_todo = {'test' : 'test', 'userId': 0, 'id': 0, 'title': 'zen in every breath', 'completed': True}
#data.append(new_todo)

r2 = requests.post('https://jsonplaceholder.typicode.com/todos', data = {'test' : 'test', 'userId': 201, 'id': 201, 'title': 'zen in every breath', 'completed': True})

data2 = r2.json()
#print(data2)
r = requests.delete('https://jsonplaceholder.typicode.com/todos/delete/1')
r = requests.get('https://jsonplaceholder.typicode.com/todos')
data = r.json()

#print(data)
for item in data:
 	print ("TODO: " + str(item) )

	# -------------------


 