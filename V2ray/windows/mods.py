# -- coding:utf-8--
from multiprocessing import Process
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json

def get_update():

	#用于获取更新的函数
	update_url = "http://60.205.221.103/v2ray/update.exe"
	gzlj = os.getcwd()
	jdlj = os.path.join(gzlj,'更新v2ray.exe')
	request.urlretrieve(update_url, jdlj)

def jc_update():
	#用于检查是否需要更新的函数
	jg = True
	update_url = "http://lucyx.cn/zzz/v2ray/update.json"
	bdupurl = r"C:\pythonz\unsers\update.json"
	request.urlretrieve(update_url, bdupurl)
	with open(bdupurl) as zx_1:
		edition = json.load(zx_1)
	if edition == 2 :
		jg = False
	else:
		jg = True
	return jg


def addlj():
	mblj_1 = r'C:\pythonz\sun36x64'
	mblj_2 = r'C:\pythonz\unsers'
	os.makedirs(mblj_1)
	os.makedirs(mblj_2)

def start_V2ray():
	os.system(r'C:\pythonz\sun36x64\v2ray\v2ray.exe')

def getv2json():
	url = "http://lucyx.cn/zzz/v2ray/v2_config_1.json"
	request.urlretrieve(url, r"C:\pythonz\sun36x64\v2ray\config.json")

def rmv2json():
	#延迟启动进行删除
	time.sleep(2)
	os.remove(r"C:\pythonz\sun36x64\v2ray\config.json")

def remove_dir(dir):
	#用于删除路径的函数
	dir = dir.replace('\\', '/')
	if(os.path.isdir(dir)):
		for p in os.listdir(dir):
			remove_dir(os.path.join(dir,p))
		if(os.path.exists(dir)):
			os.rmdir(dir)
	else:
		if(os.path.exists(dir)):
			os.remove(dir)


def now_time():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx = nowtime.strftime('%Y-%m-%d-%H-%M')
	return timexx


def wl_time(z):
	#生成未来时间的函数
	nowtime=datetime.datetime.now()
	detaday=datetime.timedelta(days=z)
	da_days=nowtime+detaday
	wltime = da_days.strftime('%Y-%m-%d-%H-%M')
	#输出返回值为 年 月 日 时 分
	return wltime

def put_key(a):
	#用于输出密钥文件的函数
	keyjson = r'C:\pythonz\unsers\key.json'
	#写入json 加密后的密钥
	with open(keyjson,'w') as ls:
		json.dump(a,ls)

def get_v2ray():
	print("正在下载V2ray资源包\n")
	print("这需要几分钟时间\n")
	#声明url
	url = "http://60.205.221.103/v2ray/v2rayWin.zip"
	url_1 = "http://lucyx.cn/zzz/v2ray/rmv2json.bat"
	#下载压缩包
	request.urlretrieve(url, r"C:\pythonz\sun36x64\V.zip")
	print("已下载完成压缩包")
	#读取压缩包
	azip = zipfile.ZipFile(r"C:\pythonz\sun36x64\V.zip")
	#解压到原始目录
	azip.extractall(r"C:\pythonz\sun36x64")
	print("已解压完成")
	print("\n如卡在此步可以按下回车")


def myyz():
	#用于验证密钥是否存在的函数
	myjson = r'C:\pythonz\unsers\key.json'
	with open(myjson) as zx:
		number = json.load(zx)
	return number
