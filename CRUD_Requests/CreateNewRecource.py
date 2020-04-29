import requests
import json
import jsonpath

url = "https://reqres.in/api/users?page=2"

# Read Json input file
file = open('/Users/ivoitkiv/PycharmProjects/APIAutomation/CreatingNewUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

#Send Post Request
response = requests.post(url,request_json)
assert response.status_code == 201

print(response.headers.get('Content-Length'))
json_response = json.loads(response.text)
id = jsonpath.jsonpath(json_response,'id')
print(id[0])