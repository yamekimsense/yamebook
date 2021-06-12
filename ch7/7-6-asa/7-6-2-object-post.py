#python3 works
#create object network

import json, requests
from requests.auth import HTTPBasicAuth

server = "https://192.168.30.232"
api_path = "/api/objects/networkobjects/"
url = server+api_path

username = "cisco"
password = "cisco"

headers = { 'content-Type' : 'application/json' }

data = {
        "kind": "object#NetworkObj",
        "name": "hostObjByApi",
        "host": {
            "kind": "IPv4Network",
            "value": "10.1.1.0/24"
            }
}

res = requests.post (url, json.dumps(data), auth=HTTPBasicAuth(username, password), verify=False, headers = headers)
print (res)
print (res.text)


'''

WANKIM-M-L2HC:7-6-asa wansookim$ python3 7-6-2-object-post.py 
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
<Response [201]>

WANKIM-M-L2HC:7-6-asa wansookim$ 


vASA96# show run object
object network host1
 host 168.126.63.1
object network hostObjByApi
 subnet 10.1.1.0 255.255.255.0
vASA96# 

'''