# -- coding:utf-8--
import multiprocessing
from urllib import request
import mods
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket

sock = socket.socket()

HOST = '45.32.169.9'
PORT = 2233

#程序入口
if __name__ == "__main__":
	multiprocessing.freeze_support()
	print('\nV2ray 启动器V1.1')
	#检测软件是否被安装过
	if os.path.exists(r'C:\pythonX'):
		try:
			#检测密钥文件是否存在
			myyz_z = mods.myyz()
		except:
			print("您还没有激活！\n")
			key = input("请输入密钥：")
            data = key
        data = myyz_z
        try:
            sock.connect((HOST, PORT))
            sock.sendall(data.encode())
            server_re = sock.recv(1024).decode()
            sock.close()
        except:
            print("连接服务器失败！")
            print("错误！X006\n")
            input("按下任意键退出程序！")
            sys.exit(0)
		if server_re == 3:
			print("密钥输入错误！\n")
			input("按下任意键退出程序！")
			sys.exit(0)
		if server_re == 2:
            print("密钥已过期！\n")
            input("按下任意键退出程序！")
			sys.exit(0)
        if server_re == 1:
            print("验证成功！\n")
			try:
				#下载配置文件
				core.mods.getv2json()
			except:
				#下载错误反馈
				print("错误！X001\n")
				input("按下任意键退出程序！")
				sys.exit(0)
			try:
				#申请一个子进程开启删除配置文件脚本
				p = multiprocessing.Process(target=core.mods.rmv2json)
				#运行脚本
				p.start()
				#主进程同时打开V2RAY
				core.mods.start_V2ray()
			except:
				#开启错误反馈
				print("错误！X003\n")
				input("按下任意键退出程序！")
				sys.exit(0)
	else:
		print("检测到此电脑并未安装V2ray\n")
		try:
			#创建路径
			mods.addlj()
		except:
			#创建路径错误反馈
			print("错误！X005\n")
			input("按下任意键退出程序！")
			sys.exit(0)
		try:
			#下载V2ray安装包并解压
			mods.get_v2ray()
		except:
			#下载错误反馈
			print("错误！X006\n")
			input("按下任意键退出程序！")
			sys.exit(0)

		print("安装成功！\n")
		print("请重新启动程序！\n")
		input("按下任意键退出程序！")
		sys.exit(0)
