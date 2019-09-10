Make a call using the Python requests library > and then store in Python object from that json > adjusted Lambda to check for request method and change response > code for lambda is below (this likely broke the JS test I did with it earlier as API Gateway also now does ANY vs the previous GET)

* Round 2 - added pipenv and verified that it's not broken after API Gateway was updated

```
import json

def lambda_handler(event, context):
    # TODO implement
    todosGET = [{ "todo1" : {'id': 1, 'name': 'getfirst'}}, 
             {"todo2": {'id': 2, 'name': 'getsecond'}}]
    todosPOST = [{'id': 1, 'name': 'postfirst'}, 
             {'id': 2, 'name': 'postsecond'}]
    
    if event["httpMethod"] == "GET":
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
                },
            'body': json.dumps(todosGET)
        }
    elif event["httpMethod"] == "POST":
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'application/json',
                'Access-Control-Allow-Origin': '*'
                },
            'body': json.dumps(todosPOST)
        }
```