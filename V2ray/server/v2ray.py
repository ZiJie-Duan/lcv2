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

print("v2ray server start！")

while True:
	try:
		#堵塞连接
		cli, addr = sock.accept()
		#打印连接pi及信息
		show_time = mods.now_time_show()
		print("")
		print(addr)
		print(show_time)
		#接收模式识别
		mod = cli.recv(2048).decode()
		print("接受模式")
		cli.sendall("my".encode())
		print("第一次对话完成")
		#接收key
		key = cli.recv(2048).decode()
		print("接受key")
		cli.sendall("my".encode())
		print("第二次对话完成")
		#接收mac
		mac = cli.recv(2048).decode()
		print("1")
		#mod1
		if mod == "mac":
			print("mod_mac start!")
			#验证mac
			ztm, time, root, x = mods.yzkey_userk(key,mac)
			if root == True:
				time = "0000-00-00-00-00"
				ml = "0"
				send = ztm + "." + time + "." + ml + "." + x
				send = "4"
				cli.sendall(send.encode())
			if ztm == "1":
				ml = "0"
				send = ztm + "." + time + "." + ml + "." + x
				cli.sendall(send.encode())
			if ztm == "2":
				ml = "0"
				send = ztm + "." + time + "." + ml + "." + x
				cli.sendall(send.encode())
			if ztm == "3":
				ml = "0"
				send = ztm + "." + time + "." + ml + "." + x
				cli.sendall(send.encode())
			print("这不可能！")
		#mod2
		if mod == "key":
			print("mod_key start!")
			#验证用户是否存在
			if yzkey_userk_cz(mac):
				#根据密钥延长时间
				fhz, time = mods.time_tjkey(key,mac)
				if fhz == "1":
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
				if fhz == "2":
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
				print("这不可能！")
			else:
				fhz, time = yzkey_keyk(key)
				if fhz == "1":
					mods.userk_xr(mac,key,time)
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
				if fhz == "2":
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
				print("这不可能！")
		#关闭连接
		cli.close()
	except:
		show_time = mods.now_time_show()
		print("\n错误！")
		print(show_time)
		print("\n") 