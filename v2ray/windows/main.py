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
		if os.path.exists(route):
			user.read_user()
			print("您的uuid为 " + mwzfc)
	else:
		#删除文件
		install.del_v2()
		#创建路径
		install.addlj()
		#v2ray服务器压缩包
		install.get_v2ray()
		print("安装完成\n请再次启动\n回车以退出程序")
		sys.exit()
