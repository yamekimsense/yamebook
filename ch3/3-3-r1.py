#python v3

import socket
import struct
import datetime

old = 0

multicast_group = '224.3.29.71'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)

# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

# Receive/respond loop
while True:

    data, address = sock.recvfrom(1024)
    data2 = int(data.decode('utf-8'))
    print ("start================")
    print ("data2 ", type(data2))

    if data2 == old:
        print ("okay #### Arrived", data2, "expected", old, datetime.datetime.now())
    else:
        print ("wrong #### Arrived ", data2, "expected ", old, datetime.datetime.now())

    sock.sendto('ack'.encode(), address)
    old = data2 + 1

    print ("data2 ", data2, "old ", old)
    print ("END =================")
    print ("                   ")
