# -- coding:utf-8--
import socket
import time
import datetime
import json
import os

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
print("v2ray server start！")

while True:
#try:
	#堵塞连接
	cli, addr = sock.accept()

	mod = cli.recv(2048).decode()

	if mod == "update":
		cli.sendall("6.0".encode())

	elif mod == "login":

		cli.sendall("my".encode())
		userid = cli.recv(2048).decode()
		cli.sendall("F".encode())


	elif mod == "logon":

		cli.sendall("my".encode())
		key = cli.recv(2048).decode()
		cli.sendall("F".encode())


	cli.close()