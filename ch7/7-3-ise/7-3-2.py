import requests

headers = {
    'Accept': 'application/json',
}

response = requests.get('https://10.72.80.184:9060/ers/config/node', headers=headers, verify=False, auth=('admin', '1234Qwer'))

print (response.text)