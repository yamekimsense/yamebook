#TTL = 10
#python3

import socket
import struct
import time
import datetime

i = 0

multicast_group = ('224.3.29.71', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 10)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)


# Send data to the multicast group

while 1>0:
 message = str(i)
 print (i, datetime.datetime.now())
 sent = sock.sendto(message.encode(), multicast_group)
 time.sleep(1)
 i = i + 1
