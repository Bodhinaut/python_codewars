# importing the requests library
import requests
 
# api-endpoint
URL = 'https://jsonplaceholder.typicode.com/todos' 

# location given here
#location = 200
 
# defining a params dict for the parameters to be sent to the API
#PARAMS = {'id':location}
 
# sending get request and saving the response as response object
r = requests.get(url = URL) #params = PARAMS
 
# extracting data in json format
data = r.json()

for item in data:
	print ("TODO: " + str(item) )
 

print("string value: %s" % data[1]['id'])