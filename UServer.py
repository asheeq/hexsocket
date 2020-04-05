#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
from kafka import KafkaProducer
from json import dumps
from time import sleep

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(("localhost", 1235))

while True:
    data, addr = serverSock.recvfrom(1024)
    str=print ("Message: " + data.decode())
    print("posted successfully.")

