import socket

def print_info():
    host_name = socket.gethostname()
    ip_addr   = socket.gethostbyname(host_name)
    print "Host name is %s" % host_name
    print "The IP address is %s" % ip_addr

if __name__ == '__main__':
    print_info() 
