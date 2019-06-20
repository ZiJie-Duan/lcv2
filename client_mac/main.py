# -- coding:utf-8--
import multiprocessing
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import ssl 

from mods import selfprotect,configread,v2raydo,user,server,delold

ssl._create_default_https_context = ssl._create_unverified_context



if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	print("lcv2 MacOS V6.2")

	update_bb = "6.2"
	sock = socket.socket()
	HOST = "www.lucycore.top"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("update".encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()

	if server_s == update_bb:
		print("版本验证成功！")

		gzlj = os.getcwd()
		user_file = gzlj + "/user.json"

		if os.path.exists(user_file):

			with open(user_file) as zx:
				userid = json.load(zx)

			sock.connect((HOST, PORT))
			#发送模式
			sock.sendall("login".encode())
			my = sock.recv(1024).decode()
			sock.sendall(userid.encode())
			zt = sock.recv(1024).decode()

			sock.close()

			if zt == "T":
				print("验证成功！")

				sock.connect((HOST, PORT))
				#发送模式
				sock.sendall("config".encode())
				pzdata = sock.recv(1024).decode()
				pzdata = pzdata.split('!')
				
				
				with open("") as zx:
					number = json.load(zx)



			else:
				print("验证失败！您的卡密不存在或已过期！")
				os.remove(user_file)
				input("请重启程序，重新激活！按下回车退出！")
				sys.exit(0)


'''
	numbers = [1,2,3,4,5,6,7,8,9]
	filename = 'numbers.json'
	with open(filename,'w') as ojbk:
		json.dump(numbers,ojbk)

	with open(filename) as zx:
		number = json.load(zx)

'''
	else:
		print("此版本已过期！请点击链接下载最新版本！")
		print("http://www.lucycore.top/v2ray/lcv2Mac.zip")
		input("按下回车后退出！")
		sys.exit(0)


		

	
