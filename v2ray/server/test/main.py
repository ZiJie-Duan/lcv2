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
	#打印连接pi及信息
	print("")
	print(addr)
	#接收模式识别
	mod = cli.recv(2048).decode()

	if mod == "update":
		cli.sendall("5.1".encode())

	if mod == "mod_1":
		cli.sendall("my".encode())
		cli.recv(2048).decode()#uuid
		cli.sendall("my".encode())
		cli.recv(2048).decode()#key
		cli.sendall("ok".encode())
		cli.recv(2048).decode()#占位
		cli.sendall("34.80.176.235*2233*2b9ce50e-65b7-42fb-861f-22c476f9f0b4".encode())

	if mod == "mod_2":
		cli.sendall("my".encode())
		cli.recv(2048).decode()#uuid
		cli.sendall("ok".encode())
		cli.recv(2048).decode()#占位
		cli.sendall("34.80.176.235*2233*2b9ce50e-65b7-42fb-861f-22c476f9f0b4".encode())


		#关闭连接
		cli.close()
	'''
	except:
		print("qazqwe")
		#关闭连接
		cli.close()
'''



