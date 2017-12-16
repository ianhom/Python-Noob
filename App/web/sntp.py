#!/usr/bin/python

import socket
import struct
import sys
import time

NTP_SERVER = "0.uk.pool.ntp.org"

TIME1970 = 2208988800L

def sntp_client():
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    data   = '\x1b' + 47 * '\0'
    client.sendto(data, (NTP_SERVER,123))
    data, address = client.recvfrom(1024)
    if data:
        print "Response received from:", address
    t = struct.unpack('!12I',datae)[10]
    t -= TIME1970

    print "time is %s" %time.ctime(t)

if __name__ =='__main__':
    sntp_client()
