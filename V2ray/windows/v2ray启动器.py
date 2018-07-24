# -- coding:utf-8--
from su.aes import encrypt, decrypt
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

mblj_1 = r'C:\pythonz4\sun36x64'

def go():

	print('\nV2ray 启动器V4.0')
	#检查更新的函数
	mods.jcgx_zt()
	if os.path.exists(mblj_1):
		#启动核心模块
		mods.core()
	else:
		#启动检测旧版本程序
		mods.old_rm()
		mods.install()



#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	go()


