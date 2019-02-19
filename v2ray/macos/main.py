# -- coding:utf-8--
import multiprocessing
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import uuid
import ssl 

from mods import install,aess,delold,script,server,start,update,user
#https协议兼容
ssl._create_default_https_context = ssl._create_unverified_context


#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	print("v2ray 启动器V5.1")

	gzlj = os.getcwd()
	#判断是否有更新
	update.update()

	#尝试运行特殊命令
	try :
		script.dtml_srjc()
	except:
		print("")

	#运行旧版本清除模块
	delold.old_rm()

	#判断v2是否安装完整
	if install.t_v2():

		#user文件路径
		userlj = os.path.join(gzlj, "pythonz5.1","unsers","user.json")

		#判断用户文件是否存在
		if os.path.exists(userlj):
			#用户文件存在
			uid = user.read_user()
			print("您的ID：" + uid)

		else:
			#用户文件不存在
			print("")

	else:
		#删除v2文件目录
		install.del_v2()
		#创建路径
		install.addlj()
		#下载安装v2本体
		install.get_v2ray()
		print("请您重启此程序！")
		input("按下回车后 关闭程序！")
		sys.exit()
		









