import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://ios-xe-mgmt-latest.cisco.com:443/restconf/data/ietf-interfaces:interfaces"

payload = {}
headers = {
  'Content-Type': 'application/yang-data+json',
  'Accept': 'application/yang-data+json'
}

response = requests.request("GET", url, headers=headers, auth=HTTPBasicAuth('developer', 'C1sco12345'), data = payload, verify=False)

print ("======== Original Response ========")

print(response)
print(response.text)
print (type (response.text))

print ("======== str to dict ========")

ifs = json.loads (response.text)
print (ifs)
print (type(ifs))

g1 = ifs['ietf-interfaces:interfaces']['interface']
print (g1)
print (type(g1))

g2 = ifs['ietf-interfaces:interfaces']['interface'][0]['name']
print (g2)
print (type(g2))
