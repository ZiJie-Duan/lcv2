# -- coding:utf-8--
from multiprocessing import Process
from urllib import request
import core.mods
import os
import shutil
import zipfile
import time
import datetime
import json 
import sys


#程序入口
if __name__ == "__main__":
	print('\nV2ray 启动器V1.1')
	#检测软件是否被安装过
	if os.path.exists(r'C:\pythonX'):
		try:
			#检测时间是否可用
			yztime = core.mods.timeyz()
		except:
			print("您还没有激活！\n")
			key = input("请输入密钥：")
			#调用jmyz函数解密
			dcz = core.mods.jmyz(key)
			if dcz == 0:
				print("密钥输入错误！\n")
				input("按下任意键退出程序！")
				sys.exit(0)
			else:
				try:
					#尝试写入时间文件
					core.mods.put_time(dcz)
				except:
					#写入失败的反馈！
					print("错误！X004\n")
					input("按下任意键退出程序！")
					sys.exit(0)
				#激活成功！
				print("激活成功！\n")
				print("请重新启动程序！\n")
				input("按下任意键退出程序！")
				sys.exit(0)

			#判断时间是否可用
		if yztime == True:			
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
				p = Process(target=core.mods.rmv2json)
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
			#时间不可用反馈
			print("您的密钥已过期！\n")
			key = input("请重新输入密钥：")
			#调用jmyz函数解密
			dcz = core.mods.jmyz(key)
			if dcz == 0:
				print("密钥输入错误！\n")
				input("按下任意键退出程序！")
				sys.exit(0)
			else:
				try:
					#尝试写入时间文件
					core.mods.put_time(dcz)
				except:
					#写入失败的反馈！
					print("错误！X004\n")
					input("按下任意键退出程序！")
					sys.exit(0)
				#激活成功！
				print("激活成功！\n")
				print("请重新启动程序！\n")
				input("按下任意键退出程序！")
				sys.exit(0)

	else:
		print("检测到此电脑并未安装V2ray\n")
		try:
			#创建路径
			core.mods.addlj()
		except:
			#创建路径错误反馈
			print("错误！X005\n")
			input("按下任意键退出程序！")
			sys.exit(0)
		try:
			#下载V2ray安装包并解压
			core.mods.get_v2ray()
		except:
			#下载错误反馈
			print("错误！X006\n")
			input("按下任意键退出程序！")
			sys.exit(0)

		print("安装成功！\n")
		print("请重新启动程序！\n")
		input("按下任意键退出程序！")
		sys.exit(0)
