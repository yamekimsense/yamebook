import requests, json

mac = "00:01:02:03:99:99"

headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

#GET Identity Group ID of <YAME>
response = requests.get('https://10.72.80.184:9060/ers/config/endpointgroup/name/yame', headers=headers, verify=False, auth=('admin', '1234Qwer'))
dicttt = json.loads(response.text)
gID = dicttt['EndPointGroup']['id']

#Insert MAC to YAME

data = ' { "ERSEndPoint" : { "name" : "Assets_Endpoint", "description" : "Another asset", "mac" : "' + mac + '", "groupId" : "' + gID + '", "staticGroupAssignment" : true } }'
response = requests.post('https://10.72.80.184:9060/ers/config/endpoint', headers=headers, data=data, verify=False, auth=('admin', '1234Qwer'))
print (response)
