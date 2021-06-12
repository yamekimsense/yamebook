from elasticsearch import Elasticsearch
import Adafruit_DHT as dht
import time, os, datetime

h,t = dht.read_retry(dht.DHT11, 4)

es = Elasticsearch('http://192.168.30.146:9200')
doc = {
 "humid" : int(round(t)),
 "temp" : int(round(h)),
 "time" : datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
}
res = es.index(index="pip9", doc_type="_doc", body = doc)

print ("Humid ", h, "Temp ", t)
print (res)