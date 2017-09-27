# sACN playback

# takes in csv list of values to playback over dmx

import math

from packet import E131Packet
from source import DMXSource

data = [255] * 512

p = E131Packet(universe=1, data=data)


import socket
import struct
import csv
import time
import io


# 239.256.0.1:5568
UDP_IP = "239.255.0.1"

UDP_PORT = 5568
multicast_group = ("239.255.0.1", 5568)

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP

# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.5)

# sent = sock.sendto(p.packet, (UDP_IP, UDP_PORT))
src = DMXSource()
outputList = []
# Open file with dmx data
with io.open('test.csv', 'r') as f:
    reader = csv.reader(f)
    listdata = list(reader)

    for row in listdata:
        outputList.append(map(int, row))

    print "Number of frames " + str(len(listdata))

print "Starting Loop"
# write data out to network in loop
while 1 == 1:

    for row in outputList:
            src.send_data(row)
            time.sleep(0.05)

