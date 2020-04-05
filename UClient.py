#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import json
li = []
s = ""
UDP_IP_ADDRESS = "localhost"
UDP_PORT_NO = 1235
clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
file = open("/home/asheeq/Downloads/netflowsample.txt","rb")
f = file.readlines()
array = bytearray(f[0])
for i in array:
    s+=str(chr(i))
    if(len(s)==2):
        li.append(s)
        s = ""
#Sending element
for j in li:
    clientSock.sendto(j.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))
#Sending as a list
#data = json.dumps(li)
#clientSock.sendto(data.encode(), (UDP_IP_ADDRESS, UDP_PORT_NO))

