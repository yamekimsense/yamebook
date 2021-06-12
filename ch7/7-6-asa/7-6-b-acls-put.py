
import json, requests
from requests.auth import HTTPBasicAuth

server = "https://192.168.30.232"
api_path = "/api/objects/extendedacls/ACL1/aces"
url = server+api_path

username = "cisco"
password = "cisco"

headers = { 'content-Type' : 'application/json' }

res = requests.get (url, verify=False, auth=HTTPBasicAuth(username, password), headers = headers)
full_path0 = json.loads(res.text)["items"][0]['selfLink']
full_path1 = json.loads(res.text)["items"][1]['selfLink']
print (full_path0) #first line ACL URL with ID
print (full_path1) #Second line ACL URL with ID

data ={
  "sourceService": {
    "kind": "NetworkProtocol",
    "value": "ip"
  },
    "destinationService": {
    "kind": "NetworkProtocol",
    "value": "ip"
  },
  "destinationAddress": {
    "kind": "IPv4Network",
    "value": "30.3.3.0/24"
  },
  "permit": "false",
  "active": "true",
  "sourceAddress": {
    "kind": "IPv4Network",
    "value": "33.3.3.0/24"
  }
}

res = requests.put (full_path1, data=json.dumps(data), auth=HTTPBasicAuth(username, password), verify=False, headers = headers)
print (res)

'''
vASA96# show run access-list 
access-list 100 extended permit ip host 1.1.1.1 11.11.11.0 255.255.255.0 
access-list 100 extended permit ip host 2.2.2.2 22.22.22.0 255.255.255.0 
access-list ACL1 extended permit ip host 1.1.1.1 11.11.11.0 255.255.255.0 
access-list ACL1 extended deny ip 33.3.3.0 255.255.255.0 30.3.3.0 255.255.255.0 

WANKIM-M-L2HC:7-6-asa wansookim$ python3 7-6-b-acls-put.py 
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
https://192.168.30.232/api/objects/extendedacls/ACL1/aces/1897242105
https://192.168.30.232/api/objects/extendedacls/ACL1/aces/1755642224
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
<Response [204]>

'''