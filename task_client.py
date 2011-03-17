import sys
import time
import zmq


context = zmq.Context()

# get work
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# send results
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")


while True:
	s = receiver.recv()
	print "Sleeping ", s, " msec "
	time.sleep(int(s) * 0.001)
	sender.send(s)



