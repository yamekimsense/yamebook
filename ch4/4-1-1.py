import getpass
import telnetlib

HOST = input("Enter the hos IP: ")
user = input("Enter your remote account: ")

password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"show ver\n");tn.write(b"\n\n")
tn.write(b"show ip int br\n");tn.write(b"\n\n")
tn.write(b"show cdp nei \n");tn.write(b"\n\n")
tn.write(b"show cdp nei det\n");tn.write(b"\n\n")
tn.write(b"show logg\n");tn.write(b"\n\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))


with open(HOST + ".txt", 'w') as myfile:
    myfile.write(tn.read_all().decode('ascii'))
    myfile.close()

