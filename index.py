import json
import requests

todos = requests.get('https://hlv7793ve8.execute-api.us-east-1.amazonaws.com/jsontest')

todoslist = json.loads(todos.text)
print(todoslist[0])