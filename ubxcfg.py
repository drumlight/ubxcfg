#!/usr/bin/python
# 
# Jake Hawkins
# 
# Ublox Configuration. Converts ASCI config file to binary format and sends to GPS
# 
# Usage:
# 
#  ubxcfg.py [UBlox Config File] [port] [baud_default] [baud_programed]
#
# 

import binascii, serial, sys
from time import sleep

header = bytearray.fromhex('b5 62')
inputfile = open(sys.argv[1])
# outputfile= open('SAM8.bin', 'w+')
s = serial.Serial(port=sys.argv[2], baudrate=sys.argv[3], timeout=1)
postponed_commands = []

for line in inputfile:
    cs0=0
    cs1=0
    payload_bin = bytearray()
    payload_bin += header
    message=(line[:line.find(' - ')])
    payload_hex=(line[(3+line.find(' - ')):]).split()
    for d in payload_hex:
        c = binascii.unhexlify(d)
        payload_bin += c
        cs0 += ord(c)
        cs0 &= 255
        cs1 += cs0
        cs1 &= 255
    payload_bin += bytes([cs0])
    payload_bin += bytes([cs1])
    if message == 'CFG-PRT':
        postponed_commands.append(payload_bin)
    elif message == 'MON-VER':
        pass
    else:
        s.write(payload_bin)
        s.write(b'\n')
        sleep (0.05)

for line in postponed_commands:
        s.write(line)
        s.write(b'\n')
        sleep (0.05)    

inputfile.close()
s.baudrate = sys.argv[4]