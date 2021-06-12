from tcp_latency import measure_latency
from elasticsearch import Elasticsearch
import time, os, datetime

es = Elasticsearch('192.168.235.196:9200')

while 1>0:
    result = measure_latency(host='www.yahoo.com', port=80, runs=1, timeout=2)
    lat = round(result[0])
    now = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
    print (now, lat)
    doc = {
     "latency": lat,
     "time": now
    }

    es.index(index="yahoo", doc_type="_doc", body=doc)
    time.sleep(10)
