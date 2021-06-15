import json
import requests

r = requests.get("https://jsonplaceholder.typicode.com/todos/2")
test = r.json()
json_string = json.dumps(test)

print(test['title'])
