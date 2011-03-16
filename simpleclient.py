import zmq

context = zmq.Context()


print "Client"
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

for request in range(1,10):
	print "Sending request ", request, "..."
	socket.send("HELLO")
	message = socket.recv()
	print "Recv ", request, "[", message, "]"
