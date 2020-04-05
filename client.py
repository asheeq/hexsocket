#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import binascii

UDP_IP_ADDRESS = "localhost"
UDP_PORT_NO = 1234
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file = open("/home/asheeq/Downloads/netflowsample.txt","rb")
f = file.readlines()
msg = binascii.unhexlify(f[0].strip())
clientSock.sendto(msg, (UDP_IP_ADDRESS, UDP_PORT_NO))

