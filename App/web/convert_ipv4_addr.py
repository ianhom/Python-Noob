import socket
from binascii import hexlify

def cvrt_ipv4_addr():
    for ip_addr in ['127.0.0.1','192.168.0.1']:
        packed_addr   = socket.inet_aton(ip_addr)
        unpacked_addr = socket.inet_ntoa(packed_addr)
        print "IP addr is %s -->packed: %s, unpacked: %s" \
              %(ip_addr, hexlify(packed_addr),unpacked_addr)
              
if __name__ == '__main__':
    cvrt_ipv4_addr()
