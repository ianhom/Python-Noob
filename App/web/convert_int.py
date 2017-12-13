#!/usr/bin/python

import socket

def cvt_int():
    data = 1234
    print "Original: %s -> long host byte order: %s, Network byte order: %s" \
          %(data, socket.ntohl(data),socket.htonl(data))
    print "Origianl: %s -> short host byte order: %s, Network byte order: %s" \
          %(data, socket.ntohs(data),socket.htons(data))

if __name__ == '__main__':
    cvt_int()
