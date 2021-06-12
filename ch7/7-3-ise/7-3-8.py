import requests, json

mac ="00:01:02:03:99:99"
macfilter ="mac.EQ." + mac

headers = {
    'Accept': 'application/json',
}

### MAC ID

params = (
    ('filter', macfilter),
)

response = requests.get('https://10.72.80.184:9060/ers/config/endpoint', headers=headers, params=params, verify=False, auth=('admin', '1234Qwer'))
dicttt = json.loads(response.text)
macID = dicttt['SearchResult']['resources'][0]['id']

print (macID)


### Delete MAC ID

deleteurl = "https://10.72.80.184:9060/ers/config/endpoint/" + macID
response = requests.delete(deleteurl, headers=headers, verify=False, auth=('admin', '1234Qwer'))

print (response)
print (response.text)

