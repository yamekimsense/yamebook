#python3

import json, requests
from requests.auth import HTTPBasicAuth

server = "https://192.168.30.232"
api_path = "/api/objects/extendedacls/ACL1/aces"
url = server+api_path

username = "cisco"
password = "cisco"

headers = { 'content-Type' : 'application/json' }

data ={
      "permit": "true",
      "sourceAddress": {
        "kind": "IPv4Address",
        "value": "1.1.1.1"
      },
      "destinationAddress": {
        "kind": "IPv4Network",
        "value": "11.11.11.0/24"
      },
      "sourceService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "destinationService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "active": "true",
      "position": "1"
}

res = requests.post (url, data=json.dumps(data), auth=HTTPBasicAuth(username, password), verify=False, headers = headers)
print (res)

data = {
      "permit": "true",
      "sourceAddress": {
        "kind": "IPv4Address",
        "value": "2.2.2.2"
      },
      "destinationAddress": {
        "kind": "IPv4Network",
        "value": "22.22.22.0/24"
      },
      "sourceService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "destinationService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "active": "true",
      "position": "2"
    }

res = requests.post (url, data=json.dumps(data), auth=HTTPBasicAuth(username, password), verify=False, headers = headers)

print (res)




'''

vASA96# show run access-list 
access-list 100 extended permit ip host 1.1.1.1 11.11.11.0 255.255.255.0 
access-list 100 extended permit ip host 2.2.2.2 22.22.22.0 255.255.255.0 
access-list ACL1 extended permit ip host 1.1.1.1 11.11.11.0 255.255.255.0 
access-list ACL1 extended permit ip host 2.2.2.2 22.22.22.0 255.255.255.0 
vASA96# 




#python3

import json, requests
from requests.auth import HTTPBasicAuth

server = "https://192.168.30.232"
api_path = "/api/objects/extendedacls/ACL1/aces"
url = server+api_path

username = "cisco"
password = "cisco"

headers = { 'content-Type' : 'application/json' }

data ={
      "permit": "true",
      "sourceAddress": {
        "kind": "IPv4Address",
        "value": "1.1.1.1"
      },
      "destinationAddress": {
        "kind": "IPv4Network",
        "value": "11.11.11.0/24"
      },
      "sourceService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "destinationService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "active": "true",
      "position": "1"
}

res = requests.post (url, data=json.dumps(data), auth=HTTPBasicAuth(username, password), verify=False, headers = headers)
print (res)

data = {
      "permit": "true",
      "sourceAddress": {
        "kind": "IPv4Address",
        "value": "2.2.2.2"
      },
      "destinationAddress": {
        "kind": "IPv4Network",
        "value": "22.22.22.0/24"
      },
      "sourceService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "destinationService": {
        "kind": "NetworkProtocol",
        "value": "ip"
      },
      "active": "true",
      "position": "2"
    }

res = requests.post (url, data=json.dumps(data), auth=HTTPBasicAuth(username, password), verify=False, headers = headers)

print (res)

'''