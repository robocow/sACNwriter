# sACN playback

# takes in csv list of values to playback over dmx



import math
import socket
import struct
import csv
import time
import io

def colourwheel(angle):
    blue = angle % 255
    green = (angle + 85) % 255
    red = (angle + 170) % 255
    return [red, green, blue]



from packet import E131Packet
from source import DMXSource

data = [0] * 512
p = E131Packet(universe=1, data=data)

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
sock.settimeout(0.2)

# sent = sock.sendto(p.packet, (UDP_IP, UDP_PORT))
src = DMXSource()
outputList = []
# Open file with dmx data
with io.open('bgchase.csv', 'r') as f:
    reader = csv.reader(f)
    listdata = list(reader)

    for row in listdata:
        outputList.append(map(int, row))

framecounter = 0
effectRowList = []

frame = [0] * 512

# write data out to network in loop
while True:

        if framecounter < 255:
            framecounter += 1
        else:
            framecounter = 0

        for x in range(len(frame)-2):
            if (x) % 3 == 0:
                colourresult = colourwheel(x + framecounter)
                frame[x] = colourresult[0]
                frame[x + 1] = colourresult[1]
                frame[x + 2] = colourresult[2]

        src.send_data(frame)

        time.sleep(0.015)



