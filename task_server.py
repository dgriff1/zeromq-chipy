
import zmq
import random
import time


context = zmq.Context()


sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

print "Waiting"
_ = raw_input()
print "Starting"

sender.send('0')


random.seed()


total_msec = 0

for task_nbr in range(100):
	workload = random.randint(1,100)
	total_msec += workload

	sender.send(str(workload))

print "Total expected cost: %s msec" % total_msec

time.sleep(1)
