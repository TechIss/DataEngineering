import sys
import requests
import json

x = sys.argv
url = requests.get("https://jsonplaceholder.typicode.com/todos"+ str(x))
title=json.loads(r)

print(title)
