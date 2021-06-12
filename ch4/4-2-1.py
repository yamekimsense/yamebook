
import paramiko
import time

ip = "192.168.30.108"
username = "cisco"
password = "cisco"

remote_conn_pre=paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip, port=22, username=username,
                        password=password,
                        look_for_keys=False, allow_agent=False)

remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(65535)
print (output.decode())

remote_conn.send("show clock\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output.decode())

remote_conn.send("conf t\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output.decode())

remote_conn.send("hostname csr1kv\n")
time.sleep(.5)
output = remote_conn.recv(65535)
print (output.decode())
