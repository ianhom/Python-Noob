# -*- coding: cp936 -*-
#！/usr/bin/python

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [before] is %d" % bufsize

    sock.setsockopt(socket.SOL_TCP, socket.TCP_NODELAY,1)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF,RECV_BUF_SIZE)

    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print "Buffer size [after] is %d" % bufsize

if __name__ == '__main__':
    modify_buff_size()


#Result
'''
Buffer size [before] is 8192
Buffer size [after] is 4096
'''
