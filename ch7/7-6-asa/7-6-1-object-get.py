#python3 works
#get network object all


import json, requests
from requests.auth import HTTPBasicAuth

server = "https://192.168.30.232"
api_path = "/api/objects/networkobjects/"
url = server+api_path

username = "cisco"
password = "cisco"
headers = {'Content-Type': 'application/json', 'User-Agent':'REST API Agent'}

res = requests.get (url, verify=False, auth=HTTPBasicAuth(username, password), headers = headers)
print (res)
print (res.text)


dicttt = json.loads(res.text)
xxx = json.dumps(dicttt, indent=4)
print (xxx)


'''
WANKIM-M-L2HC:7-6-asa wansookim$ python3 7-6-1.py 
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
<Response [200]>
{"kind":"collection#NetworkObj","selfLink":"https://192.168.30.232/api/objects/networkobjects/","rangeInfo":{"offset":0,"limit":1,"total":1},"items":[{"kind":"object#NetworkObj","selfLink":"https://192.168.30.232/api/objects/networkobjects/host1","name":"host1","host":{"kind":"IPv4Address","value":"168.126.63.1"},"objectId":"host1"}]}
{
    "kind": "collection#NetworkObj",
    "selfLink": "https://192.168.30.232/api/objects/networkobjects/",
    "rangeInfo": {
        "offset": 0,
        "limit": 1,
        "total": 1
    },
    "items": [
        {
            "kind": "object#NetworkObj",
            "selfLink": "https://192.168.30.232/api/objects/networkobjects/host1",
            "name": "host1",
            "host": {
                "kind": "IPv4Address",
                "value": "168.126.63.1"
            },
            "objectId": "host1"
        }
    ]
}
'''