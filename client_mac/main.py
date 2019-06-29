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
from mods import install_v2

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
		
		install_v2.get_v2ray()
	else:
		print("此版本已过期！请点击链接下载最新版本！")
		print("http://www.lucycore.top/v2ray/lcv2Mac.zip")
		input("按下回车后退出！")
		sys.exit(0)





'''
	numbers = [1,2,3,4,5,6,7,8,9]
	filename = 'numbers.json'
	with open(filename,'w') as ojbk:
		json.dump(numbers,ojbk)

	with open(filename) as zx:
		number = json.load(zx)

'''


		

	
