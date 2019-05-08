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


def rm():
	print("one")
	time.sleep(2)
	print("two")
	os.system(r"rm.py")

def jc_update():
	jg = True
	update_url = "http://lucyx.cn/zzz/update.json"
	request.urlretrieve(update_url, r"update.json")
	with open("update.json") as zx_1:
		edition = json.load(zx_1)
	if edition == 2 :
		jg = False
	else:
		jg = True
	return jg

if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	if jc_update():
		print("yes")
	else:
		print("no")

	p = multiprocessing.Process(target=rm)
	#运行脚本
	p.start()
	#主进程同时打开V2RAY
	s.remove(r"hi.py")