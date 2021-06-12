import json, requests
from requests.auth import HTTPBasicAuth

server = "https://192.168.30.232"
api_path = "/api/objects/networkobjects/hostObjByApi"
url = server+api_path

username = "cisco"
password = "cisco"

headers = { 'content-Type' : 'application/json' }

data = {
        "kind": "object#NetworkObj",
        "name": "hostObjByApi",
        "host": {
            "kind": "IPv4Network",
            "value": "22.2.2.0/24"
            }
}

res = requests.put (url, json.dumps(data), auth=HTTPBasicAuth(username, password), verify=False, headers = headers)
print (res)
print (res.text)

'''
WANKIM-M-L2HC:7-6-asa wansookim$ python3 7-6-3-object-put.py 
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
<Response [204]>

vASA96# show run object
object network host1
 host 168.126.63.1
object network hostObjByApi
 subnet 22.2.2.0 255.255.255.0
vASA96# 
'''