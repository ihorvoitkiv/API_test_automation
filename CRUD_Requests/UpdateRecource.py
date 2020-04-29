import requests
import json
import jsonpath

url = "https://reqres.in/api/users/2"

# Read Json input file
file = open('/Users/ivoitkiv/PycharmProjects/APIAutomation/CreatingNewUser.json', 'r')
json_input = file.read()
request_json = json.loads(json_input)
print(request_json)

#Send Put Request
response = requests.put(url,request_json)
#Response validation
assert response.status_code == 200

#print(response.headers.get('Content-Length'))
json_response = json.loads(response.text)
#id = jsonpath.jsonpath(json_response,'id')
#print(id[0])
updated_li = jsonpath.jsonpath(json_response,'updatedAt')
print(updated_li[0])