import paramiko, random, time

def cli(command):
    real=command+"\n"
    remote_conn.send(real)
    time.sleep(.5)
    output = remote_conn.recv(65535)

f = open("4-4-6.txt", 'r')
w = open("4-4-7.txt", 'w')

lines = f.readlines()

for line in lines:
    #print ("line= ", line)
    line = line.split(' ')
    ip = line[0].replace(" ","")
    username =  line[1].replace(" ","")
    password = line[2].replace(" ","").replace("\n","")

    print ("current ", ip, username, password)

    remote_conn_pre=paramiko.SSHClient()
    remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    remote_conn_pre.connect(ip, port=22, username=username, password=password,look_for_keys=False, allow_agent=False)
    remote_conn = remote_conn_pre.invoke_shell()
    
    cli("conf t")
    
    newpass = ""
    
    for i in range(1,9):
        char = random.randrange(33,127)
        newpass = newpass + chr(char)

    cli("username " + username + " privilege 15 password " + newpass )
    cli("end")

    new = ip+" "+username+" "+newpass
    print ("new ", new+"\n")
    w.write(new+"\n")

f.close()
w.close()
