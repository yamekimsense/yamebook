
import paramiko
import time

ip = "10.1.1.1"
username = "cisco"
password = "cisco"

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)


remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
print (output)

remote_conn.send("terminal leng 0 \n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output)

while 1>0:
    remote_conn.send("\n\n\n\n\n\n\n\nshow clock detail\n")
    time.sleep(.3)
    output = remote_conn.recv(65535)
    print (output)

    remote_conn.send("show wireless media-stream client summary | inc Number\n")
    #remote_conn.send("show run | inc interface\n")
    time.sleep(1)
    output = remote_conn.recv(65535)
    print (output)