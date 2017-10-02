# sACN playback
# takes in csv list of dmx values to playback over sACN / E1.31 in a loop

from source import DMXSource
import sys
import csv
import time
import io

#use argv to get command line arguments

if len(sys.argv) != 3:
    print "number of arguments found " + str(len(sys.argv))
    print "Please specify CSV file to play and the universe e.g. 'python CSVPlay.py test.csv 1'"
    exit(1)
try:
    universe_number = int(sys.argv[2])
except ValueError:
    print "Universe number not correct"
    exit(1)

#use lumen lib to send sACN packets

src = DMXSource()
src.universe = universe_number
outputList = []

# Open file with dmx data
try:
    with io.open(sys.argv[1], 'r') as f:
        reader = csv.reader(f)
        listdata = list(reader)
except OSError as e:
    print("File open failed")
    exit(1)

for row in listdata:
    outputList.append(map(int, row))    #convert type to int.

print "Number of frames " + str(len(listdata)) #check on frames read in - useful to see it rad correctly
print "Break to exit - Ctrl-C"
print "Starting Main Loop..."

# write data out to network in loop
while 1 == 1:

    for row in outputList:
            src.send_data(row)
            time.sleep(0.05)

