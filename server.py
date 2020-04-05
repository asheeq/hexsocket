#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind(("localhost", 1234))

while True:
    data, addr = serverSock.recvfrom(4096)
    str = print(data)
    print("posted successfully.")

