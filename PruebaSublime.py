#Read info from json file 
import json

with open('info.json') as json_file:
	data = json.load(json_file)
	user = data["user"]
	paswd = data["pass"]

	print(user)
print(paswd)


#elements = json.loads(file.read())
#print(elements['user'])
#print(elements['pass'])
