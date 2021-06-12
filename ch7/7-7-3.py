from puresnmp import get
from influxdb import InfluxDBClient
import time

oid = '1.3.6.1.4.1.9.9.42.1.2.10.1.1.'

while 1>0 :
    for i in range(100,600,100):
        result = get("192.168.235.5", "public", oid + str(i))
        print (i, result)
        if result == 0:
            print ("value 000")
            result = 200

        json_body = [
        {
            "measurement": i,
            "tags": {
                    "host": "server02",
                    "region": "kr"
                    },
            "fields": {
                      "value": result
                      }
        }
        ]

        client = InfluxDBClient('192.168.235.2', 8086, 'root', 'root', 'myDB')
        client.write_points(json_body)
    print (" ")
    time.sleep(60)