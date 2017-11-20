# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 22:40:41 2016

@author: zhanghc
"""

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('172.17.0.1',12001))

print s.recv(1024)

for data in ['zhang','liu','wang']:
    s.send(data)
    print s.recv(1024)

s.send('exit')
s.close()

