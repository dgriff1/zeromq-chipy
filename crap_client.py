import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Connecting"
s.connect(("localhost", 2100))
s.send('Hello, world')
data = s.recv(1024)
s.close()
print 'Received', repr(data)
