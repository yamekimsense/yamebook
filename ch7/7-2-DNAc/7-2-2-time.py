import datetime

input1 = input ("date as YYYYMMDD ")
input2 = input ("24H HHMM ")

YYYY = int(input1[0:4])
MM = int(input1[4:6])
DD = int(input1[6:8])
HH = int(input2[0:2])
Min = int(input2[2:5])
print (YYYY, MM, DD, HH, Min)

timestamp = datetime.datetime(YYYY, MM, DD, HH, Min).strftime('%s')
starttime = int(timestamp)*1000
print (starttime)

'''
WANKIM-M-L2HC:7-2-DNAc wansookim$ python3 7-2-2-time.py 
date as YYYYMMDD 20210117
24H HHMM 2000
2021 1 17 20 0
1610881200000
WANKIM-M-L2HC:7-2-DNAc wansookim$ 
'''