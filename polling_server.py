import zmq
import time
# Prepare our context and sockets
context = zmq.Context()


socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Initialize poll set
poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)

# Process messages from both sockets
while True:
	print "Polling"
	socks = dict(poller.poll(timeout=0))
	print "Poll results ", socks
	if socket in socks and socks[socket] == zmq.POLLIN:
		print "Got ", socket.recv()
		socket.send("Got it")
	time.sleep(1)
