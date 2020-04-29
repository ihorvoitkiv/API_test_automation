import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

def test_create_new_user0():
    file = open('/Users/ivoitkiv/PycharmProjects/APIAutomation/CreatingNewUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url,request_json)
    assert response.status_code == 201

def test_create_new_user1():
    file = open('/Users/ivoitkiv/PycharmProjects/APIAutomation/CreatingNewUser.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    response = requests.post(url, request_json)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'id')
    print(id[0])