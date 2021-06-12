from tcp_latency import measure_latency
import os, time
from datetime import datetime

i=0
bank = []

while 1>0:
    now = datetime.now()
    result = measure_latency(host='www.yahoo.com', port=80, runs=1, timeout=2)
    result = int ( round ( result[0] ) )

    bank.insert(i, result)
    avg = sum(bank) / (i+1)
    maxx = max(bank)
    minn = min(bank)

    print ( now, result , round( avg), maxx, minn )
    i = i + 1

    time.sleep(1)