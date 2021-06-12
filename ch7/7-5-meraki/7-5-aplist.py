import requests, json

url = "https://api.meraki.com/api/v1/networks/{network}/devices"

payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "123456789012345678901234567890"
}

response = requests.request('GET', url, headers=headers, data = payload)
response = response.text
dicttt = json.loads (response)

print (type(dicttt))
#print (dicttt)

j = len(dicttt)
print (j)

for i in range (0, j):
    ppp = dicttt[i]
    print (ppp["mac"],ppp["name"],ppp["lat"],ppp["lng"],ppp["model"] )
