# -- coding:utf-8--
import socket
import time
import datetime
import json
import os
import mods

#声明主机
host = ""
#声明端口号
port = 2233
#创建sock套接字
sock = socket.socket()
#绑定主机和端口
sock.bind((host, port))
#开始监听
sock.listen(5)
#对话循环
while True:
    #堵塞连接
    cli, addr = sock.accept()
    #打印连接pi及信息
    print(addr)
    #接收密钥
    data = cli.recv(2048).decode()
    key = data
    #验证密钥
    sen = mods.yzkey(key)
    #发送回客户端
    cli.sendall(sen.encode())
    #关闭连接
    cli.close()

