
import sys
import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)

print "Collecting updates!"
socket.connect("tcp://localhost:5556")
print "Connected"
filt = sys.argv[1] if len(sys.argv) > 1 else "10001"
socket.setsockopt(zmq.SUBSCRIBE, filt)


while True:
	string = socket.recv()
	print "Avg temp ", string
