#!/bin/python

import sys
import socket
from datetime import datetime

if len(sys.argv)==2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalid")
    print("Syntax : python3 port1.py <ip>")

# Add a pretty banner
print('-'*50)
print("Target IP is:  "+ target)
print(str("The current time  is  : "+str(datetime.now())))
print('-'*50)

try:
    for port in range(1,65535):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result  =  s.connect_ex((target,port)) # this would help in indicating error
        if result == 0 :
            print("Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print('\Exiting program')
    sys.exit()
except socket.gaierror:
    print('hostname couldnot be resolved')
    sys.exit()

except socket.error:
    print('not connect to server')
    sys.exit()
