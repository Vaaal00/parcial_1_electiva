import json

def message(event, context):
    body = {
        "message": "Hello, Juan y Valeria"
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
