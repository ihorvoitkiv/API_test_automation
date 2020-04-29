import requests
import json
import jsonpath

def test_add_new_user():
    app_url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open('/Users/ivoitkiv/PycharmProjects/APIAutomation/CreatingNewUser.json', 'r')
    request_json = json.loads(file.read())
    response = requests.post(app_url,request_json)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])

    t_skills_url ="http://www.thetestingworldapi.com/api/technicalskills"
    file = open('/Users/ivoitkiv/PycharmProjects/APIAutomation/TechnicalSkills.json', 'r')
    request_json = json.loads(file.read())
    request_json['id'] = int(id[0])
    request_json['st_id'] = id[0]
    response = requests.post(t_skills_url,request_json)
    print(response.text)

    adress_url ="http://www.thetestingworldapi.com/api/addresses"
    file = open('/Users/ivoitkiv/PycharmProjects/APIAutomation/Adress.json', 'r')
    request_json = json.loads(file.read())
    request_json['stId'] = id[0]
    response = requests.post(adress_url,request_json)
    print(response.text)

    final_details = "http://www.thetestingworldapi.com/api/api/Students/"+ str(id[0])
    response = requests.get(final_details)
    print(response.text)


