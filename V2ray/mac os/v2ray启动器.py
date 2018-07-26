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
import uuid

#工作路径
gzlj = os.getcwd()
mblj_1 = os.path.join(gzlj, "pythonz4")

def go():

	print('\nV2ray 启动器V4.0')

	if os.path.exists(mblj_1):
		#检查更新的函数
		mods.jcgx_zt()
		#启动检测旧版本程序
		mods.old_rm()
		#启动核心模块
		mods.core()
	else:
		#启动检测旧版本程序
		mods.old_rm()
		#安装最新v2
		mods.install()



#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	go()


