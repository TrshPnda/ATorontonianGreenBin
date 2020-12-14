#!/usr/bin/python3

import socket
import sys

def connect():
        RHOST = sys.argv[1]
        RPORT = int(sys.argv[2])
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print ("connecting to %s port %s"% (RHOST, RPORT))
        sock.connect((RHOST, RPORT))
        sock.close()

connect()
