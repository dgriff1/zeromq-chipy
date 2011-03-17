import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 2100))
print "Listening"
s.listen(1)
while 1:
	conn, addr = s.accept()
	print 'Connected by', addr
	data = conn.recv(1024)
	print "Got ", data
	if not data: 
		break
	conn.send(data * 2)
	conn.close()
