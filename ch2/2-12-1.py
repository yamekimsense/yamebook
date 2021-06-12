import requests

response = requests.get("http://www.cisco.com")

print (response.status_code)
