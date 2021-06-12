from threading import Thread
import time, getpass, sys, telnetlib

def work(i, id, password, enable, network):
    HOST = network + str(i)

    print (HOST)

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(id.encode('ascii') + b"\n")

    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

    #if enable password is needed, use this section
    #tn.write(b"enable\n")
    #tn.write(enable.encode('ascii') + b"\n")
    #tn.write(b"\n\n")

    tn.write(b"terminal length 0\n");
    tn.write(b"\n\n")
    tn.write(b"show ver\n");
    tn.write(b"\n\n")
    tn.write(b"show ip int br\n");
    tn.write(b"\n\n")
    tn.write(b"show cdp nei \n");
    tn.write(b"\n\n")
    tn.write(b"show cdp nei det\n");
    tn.write(b"\n\n")
    tn.write(b"show module\n");
    tn.write(b"\n\n")
    tn.write(b"show logg\n");
    tn.write(b"\n\n")
    tn.write(b"exit\n")

    with open(HOST + ".txt", 'w') as myfile:
        myfile.write(tn.read_all().decode('ascii'))
        myfile.close()

    return


if __name__ == "__main__":
    id = "cisco"
    password = "cisco"
    enable = "cisco"
    net = "192.168."

    for j in range (30, 31):
        network = net + str(j) + "."

        for i in range(0, 256):
            th = Thread(target=work, name=i, args=(i, id, password, enable, network))
            th.start()
            time.sleep(0.1)

print("Now getting information from network devices. Pls, wait until time out! ")