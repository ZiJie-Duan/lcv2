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

#工作路径
gzlj = os.getcwd()
mblj_1 = os.path.join(gzlj, "pythonz", "sun36x64")

#key json本地位置
key_json_lj = os.path.join(gzlj, "pythonz", "unsers", "key.json")


def go():
	gzlj = os.getcwd()
	gx_jdlj = os.path.join(gzlj,'更新v2ray.exe')

	print('\nV2ray 启动器V2.4')

	#检测软件是否被安装过
	if os.path.exists(mblj_1):
		#检查是否有更新
		if mods.jc_update():
			print("已检查到更新！\n")
			if os.path.exists(gx_jdlj):
				print("请关闭此应用后\n")
				print("点击此文件根目录下的‘更新v2ray.exe’\n")
				input("按下回车后关闭此应用！")
				sys.exit(0)
			try:
				print("正在下载更新文件！\n")
				mods.get_update()
				print("已完成下载！\n")
				print("请关闭此应用后\n")
				print("点击此文件根目录下的‘更新v2ray.exe’\n")
				input("按下回车后关闭此应用！")
			except:
				print("更新失败!")
				print("错误！x004\n")
				input("按下任意键退出程序！")
			sys.exit(0)
		try:
			#检测密钥文件是否存在
			myyz_z = mods.myyz()
			data = myyz_z
		except:
			print("您还没有激活！\n")
			key = input("请输入密钥：")
			data = key
			try:
				jm_key = "lucycore" + key
				#尝试写入密钥json
				mods.put_key(jm_key)
			except:
				print("写入失败！")
				print("错误！X007\n")
				input("按下任意键退出程序！")
				sys.exit(0)
		try:
			#创建套接字
			sock = socket.socket()
			HOST = '60.205.221.103'
			PORT = 2233
			sock.connect((HOST, PORT))
			sock.sendall(data.encode())
			server_re = sock.recv(1024).decode()
			server_time = sock.recv(1024).decode()
			sock.close()
		except:
			print("连接服务器失败！")
			print("错误！X010\n")
			input("按下任意键关闭程序！")
			sys.exit(0)
		if server_re == "3":
			print("密钥输入错误！\n")
			os.remove(key_json_lj)
			print("请重新启动再次输入")
			input("按下任意键重启程序！")
			go()
		if server_re == "2":
			print("密钥已过期！\n")
			os.remove(key_json_lj)
			print("按下任意键重启程序！")
			input("用于重新激活程序")
			go()
		if server_re == "1":
			print("验证成功！\n")
			print("到期时间：" + server_time)
			print("")
			try:
				#下载配置文件
				mods.getv2json()
			except:
				#下载错误反馈
				print("错误！X001\n")
				input("按下任意键退出程序！")
				sys.exit(0)
			try:
				#申请一个子进程开启删除配置文件脚本
				p = multiprocessing.Process(target=mods.rmv2json)
				#运行脚本
				p.start()
				#主进程同时打开V2RAY
				mods.start_V2ray()
			except:
				#开启错误反馈
				print("错误！X003\n")
				input("按下任意键退出程序！")
				sys.exit(0)
		print("您的网络速度对v2ray的影响较大")
		print("网络延迟较高")
		input("按下任意键退出程序！")
		sys.exit(0)
	else:
		try:
			print("检测到此电脑并未安装最新的V2ray\n")
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
		print("正在重新启动程序！\n")
		go()


#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	go()


