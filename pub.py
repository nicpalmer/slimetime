#!/usr/bin/env python

import zmq
import random
import sys
import time

print zmq.pyzmq_version()

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

while True:

# Needs work but this is a simple pub server
