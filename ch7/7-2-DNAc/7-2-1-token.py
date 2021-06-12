import requests
from requests.auth import HTTPBasicAuth
import json

token = requests.post(
   "https://10.72.78.17/dna/system/api/v1/auth/token",
   auth = HTTPBasicAuth ( username = "admin", password = "C1sco12345"),
   headers = { 'content-type': 'application/json' }, verify=False )
data = token.json()

print ("-------------------------------------------")
print (type(data))
print ("-------------------------------------------")
print (data)

'''
WANKIM-M-L2HC:7-2-DNAc wansookim$ python3 7-2-1-token.py 
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
-------------------------------------------
<class 'dict'>
-------------------------------------------
{'Token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1ZjVhMGIwODI2ZmMwZjAwYzg2YWQ4OTYiLCJhdXRoU291cmNlIjoiaW50ZXJuYWwiLCJ0ZW5hbnROYW1lIjoiVE5UMCIsInJvbGVzIjpbIjVmNWEwYjA4MjZmYzBmMDBjODZhZDg5NSJdLCJ0ZW5hbnRJZCI6IjVmNWEwYjA3MjZmYzBmMDBjODZhZDg5MyIsImV4cCI6MTYxMDkwMDUzMywiaWF0IjoxNjEwODk2OTMzLCJqdGkiOiJjOTk3MTNiOC0xNDBiLTQwN2YtODFiMy1mNjhmYzdmOTliZTEiLCJ1c2VybmFtZSI6ImFkbWluIn0.fbV8wm81eo90HlHRvRf48SOX0yXzh7JNa38-ja9QqOGPgYIGxzG3KaMCcIQ6Irmzzy3cy69nyNfXhh9vjQfFsyn2AQKKyFYvM5b1IssULYi-NYHac7CLdGKdZ7wBDPhN8Fkkjcb3ED8tA_ekGeyK1w-98bUHgzZM2VtXaNkE4ieyhSHAFcDEdLjzt0ZR2KYzDnQ6AFA3mIUU8qZgzmHJuMKgJAjOLPi36n7sbIQtO0Ihb7PVZRkJ-ZT9kjwZWd6HYJsR2Mo4_1Ra6VNSeCt7g0iAFZCo3PDYRx65ZlMKN2rmA3VhRUPEgK7-rccaW2MteVpYh69ye4cEFzcTKKxOTQ'}
WANKIM-M-L2HC:7-2-DNAc wansookim$ 
'''