import socket

def get_remote_machine_info():
    host_name = 'www.python.org'
    ip_addr   = socket.gethostbyname(host_name)
    print "Host name is %s" % host_name
    print "The IP address is %s" % ip_addr

if __name__ == '__main__':
    get_remote_machine_info() 
