import http.client
import ssl
import json
import requests
from requests.auth import HTTPBasicAuth
import time, datetime

#from dnac_config import DNAC, DNAC_PORT, DNAC_USER, DNAC_PASSWORD
url = 'https://IP_ADDRESS/dna/system/api/v1/auth/token'
resp = requests.post(url, auth=HTTPBasicAuth("ID", "password"), verify=False)
#print (resp)
token = resp.json()['Token']
#print("Token Retrieved: {}".format(token))


#unix time

input1 = input ("date as YYYYMMDD ")
input2 = input ("24H HHMM ")
input3 = input ("How many hours? ")

YYYY = int(input1[0:4])
MM = int(input1[4:6])
DD = int(input1[6:8])
HH = int(input2[0:2])
Min = int(input2[2:5])
#print (YYYY, MM, DD, HH, Min)

timestamp = datetime.datetime(YYYY, MM, DD, HH, Min).strftime('%s')
starttime = int(timestamp)*1000
#print (starttime)

endtime = starttime + (int(input3) * 3600000) +1


#mac
mac = input ("MAC address as 11:22:33:44:55:66 ")


#main
conn = http.client.HTTPSConnection("10.72.78.17", context = ssl._create_unverified_context())

headers = {
    'x-auth-token': token,
    'content-type': 'application/json'
    }

while starttime < endtime:
    timestamp = time.ctime(starttime)
    query = "/dna/intent/api/v1/client-detail?timestamp=" + str(starttime) + "&macAddress=" + mac
    conn.request("GET", query, headers=headers)
    res = conn.getresponse()
    data = res.read()
    realdata = json.loads(data.decode("utf-8"))
    #print (json.dumps(realdata, indent=8))
    apname = realdata['detail']['clientConnection']

    printtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(starttime/1000))
    print (starttime, printtime, mac, apname)
    starttime = starttime + 900000



'''
WANKIM-M-L2HC:7-2-DNAc wansookim$ python3 7-2-3-client.py
/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/urllib3/connectionpool.py:857: InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
  InsecureRequestWarning)
date as YYYYMMDD 20210117
24H HHMM 0500
How many hours? 2
MAC address as 11:22:33:44:55:66 54:05:DB:1A:64:19
1610827200000 2021-01-17 05:00:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610828100000 2021-01-17 05:15:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610829000000 2021-01-17 05:30:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610829900000 2021-01-17 05:45:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610830800000 2021-01-17 06:00:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610831700000 2021-01-17 06:15:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610832600000 2021-01-17 06:30:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610833500000 2021-01-17 06:45:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
1610834400000 2021-01-17 07:00:00 54:05:DB:1A:64:19 edge-1.sda.cisco.com
WANKIM-M-L2HC:7-2-DNAc wansookim$

'''