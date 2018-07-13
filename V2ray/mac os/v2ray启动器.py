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

#工作路径
gzlj = os.getcwd()
mblj_1 = os.path.join(gzlj, "pythonz3", "sun36x64")

def go():

	print('\nV2ray 启动器V3.0\n')

	#检测软件是否被安装过
	if os.path.exists(mblj_1):
		#检查是否有更新
		mods.jcgx_zt()
		#启动核心模块
		mods.server_socks_zt()

	else:
		#启动检测旧版本程序
		mods.old_rm()
		mods.installer()

#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	go()

