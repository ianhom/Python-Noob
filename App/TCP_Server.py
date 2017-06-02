
import socket  
  
address = ('192.168.1.176', 8080)  
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # s = socket.socket()  
s.bind(address)  
s.listen(5)  
  
ss, addr = s.accept()  
print 'got connected from',addr  
  
ss.send('Hello')  
while True:
    ra = ss.recv(512)
    print ra    
    ss.send(ra)  

ss.close()  
s.close()  
