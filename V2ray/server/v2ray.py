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
		cli.sendall("my".encode())
		#接收key
		key = cli.recv(2048).decode()
		cli.sendall("my".encode())
		#接收mac
		mac = cli.recv(2048).decode()
		#mod1
		if mod == "mac":
			print("mod_mac start!")
			#验证mac
			ztm, time, root, x = mods.yzkey_userk(key,mac)
			if root == True:
				print("超级用户接入 允许连接")
				time = "0000-00-00-00-00"
				ml = "0"
				ztm = "100"
				ztmh = "4"
				send = ztmh + "." + time + "." + ml + "." + x
				cli.sendall(send.encode())
			if ztm == "1":
				print("mac验证通过 允许连接")
				ml = "0"
				send = ztm + "." + time + "." + ml + "." + x
				cli.sendall(send.encode())
			if ztm == "2":
				print("mac不存在 拒绝连接")
				ml = "0"
				send = ztm + "." + time + "." + ml + "." + x
				cli.sendall(send.encode())
			if ztm == "3":
				print("时间过期 拒绝连接")
				ml = "0"
				send = ztm + "." + time + "." + ml + "." + x
				cli.sendall(send.encode())
		#mod2
		if mod == "key":
			print("mod_key start!")
			#验证用户是否存在
			if mods.yzkey_userk_cz(mac):
				#根据密钥延长时间
				fhz, time = mods.time_tjkey(key,mac)
				if fhz == "1":
					print("延长成功 允许连接")
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
				if fhz == "2":
					print("密钥不存在 拒绝连接")
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
			else:
				fhz, time = mods.yzkey_keyk(key)
				if fhz == "1":
					print("创建mac 允许连接")
					print("")
					mods.userk_xr(mac,key,time)
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
				if fhz == "2":
					print("密钥不存在 拒绝连接")
					ml = "0"
					send = fhz + "." + time + "." + ml
					cli.sendall(send.encode())
		#mod3
		#if mod == "tool":


		print("")
		#关闭连接
		cli.close()
	except:
		show_time = mods.now_time_show()
		print("\n错误！")
		print(show_time)
		print("\n") 