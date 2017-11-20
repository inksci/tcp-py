#!/usr/bin/env python

#coding=utf8



from socket import *

host = '172.17.0.1'

port = 12002

bufsiz = 1024



#开启套接字

tcpCliSock = socket(AF_INET, SOCK_STREAM)

#连接到服务器

tcpCliSock.connect((host, port))



while True:

#等待输入

    data = raw_input('> ')

    if not data:

        break

    #发送信息

    tcpCliSock.send(data)

    #接受返回信息

    response = tcpCliSock.recv(bufsiz)

    if not response:

        break

    print response

 

tcpCliSock.close()