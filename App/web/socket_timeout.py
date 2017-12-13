#!/usr/bin/python

import socket

def sck_timeout():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print "Default socket timeout is %s" %s.gettimeout()
    s.settimeout(100)
    print "Current socket timeout is %s" %s.gettimeout()

if __name__ == '__main__':
    sck_timeout()
