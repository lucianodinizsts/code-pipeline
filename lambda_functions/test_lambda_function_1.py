import json
from lambda_function_1 import lambda_handler

def test_lambda_handler():
    event = {}
    context = {}
    response = lambda_handler(event, context)
    assert response['statusCode'] == 200
    assert json.loads(response['body']) == "Olá, sou a função 1"
