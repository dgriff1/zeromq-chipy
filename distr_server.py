import zmq
import random
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
	zipcode = random.randrange(10000,10004)
	temperature = random.randrange(1,215) - 80
	relhumid = random.randrange(1,50) + 10
	print "Sending to  ", zipcode
	socket.send("%d %d %d" % (zipcode, temperature, relhumid))
	time.sleep(1)
