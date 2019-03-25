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

	print("v2ray启动器 V5.1")

	#检查是否有更新
	user.update()

	#删除旧版本
	user.old_rm()

	#判断文件是否安装
	if install.t_v2():

		#定义路径
		route = r"C:\pythonz5.1\unsers\user.json"

		#判断用户文件是否存在
		if os.path.exists(route):

			#读取uuid
			user.read_user()

			print("您的ID：" + mwzfc)

			#连接服务器获取服务器返回值
			ztm, js = server.mod_2(uid)

			#判断服务器是否允许连接
			if ztm == "T":
				#写入json并启动
				start.start_v2(js)

			else:
				user.d_id()
				print("您的账户已过期！正在移除您的账户！")
				print("请您重启此程序！")
				input("按下回车后退出程序！")
				sys.exit()
	else:
		#删除文件
		install.del_v2()

		#创建路径
		install.addlj()
		
		#v2ray服务器压缩包
		install.get_v2ray()
		print("安装完成\n请再次启动\n回车以退出程序")
		sys.exit()
                                                                                                                                                                       