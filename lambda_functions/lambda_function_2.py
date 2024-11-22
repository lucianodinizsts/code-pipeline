import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps("Olá, sou a função 2")
    }
