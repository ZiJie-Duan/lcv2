# -- coding:utf-8--
import socket
import time
import datetime
import json
import os
from mods import c_json,core,rz

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
	show_time = core.now_time_show()
	print("")
	print(addr)
	print(show_time)
	#接收模式识别
	mod = cli.recv(2048).decode()
	cli.sendall("my".encode())

	if mod == "mod_1":
		#普通登陆模式
		r = 0
		#接受uuid
		uuid = cli.recv(2048).decode()
		ztm,time,root,x = core.yzkey_userk(uuid)
		if root == True:
			cli.sendall("root.True".encode())
			r = 1
		if r == 0:
			if ztm == "1":
				#允许登陆状态
				send = ztm + "." + time + "." +  c_json.read_v2_json() + "." +  c_json.read_gg() + "." +  x
				cli.sendall(send.encode())
			if ztm == "2":
				#时间到期的处理方式
				send = ztm + "." +  time + "." +  c_json.read_v2_json() + "." +  c_json.read_gg() + "." +  x
				cli.sendall(send.encode())
			if ztm == "3":
				#uuid严重错误！
				send = ztm + "." +  time + "." +  c_json.read_v2_json() + "." +  c_json.read_gg() + "." +  x
				cli.sendall(send.encode())
		else:
			r == 0


	if mod == "mod_2":
		#增加时间模式
		#接受uuid
		uuid = cli.recv(2048).decode()
		cli.sendall("my".encode())
		#接受key
		key = cli.recv(2048).decode()
		send, time = core.yzkey_keyk(key)
		if send == "True":
			#发送状态
			cli.sendall(send.encode())
		else:
			#发送状态
			cli.sendall(send.encode())

	if mod == "mod_3":
		#注册模式
		#接收 uuid
		idu = cli.recv(2048).decode()
		#进行注册
		c_json.userk_xr(idu)
		#发送状态
		cli.sendall("True".encode())


	if mod == "update":
		#发送状态
		my = cli.recv(2048).decode()
		cli.sendall("5.1".encode())

	#关闭连接
	cli.close()
	print("over\n\n")
	'''
	
	except:
		show_time = core.now_time_show()
		print("\n错误！")
		print(show_time)
		print("\n") 
	'''