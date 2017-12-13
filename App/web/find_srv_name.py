import socket

def find_srv_name():
    ptcl = 'tcp'
    for port in [80,25]:
        print "Port is %s --> service name is %s" %(port, socket.getservbyport(port,ptcl))
        print "Port is %s --> service name is %s" %(53, socket.getservbyport(53,'udp'))
        
if __name__ == '__main__':
    find_srv_name()
