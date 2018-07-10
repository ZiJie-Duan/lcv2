# -- coding:utf-8--
from multiprocessing import Process
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json

#工作路径
gzlj = os.getcwd()
#是否有更新验证文件位置
update_json_url = "http://lucyx.cn/zzz/v2ray/update.json"
#服务器更新文件位置
update_exe_url = "http://60.205.221.103/v2ray/update.exe"
#更新验证文件位置
up_json_lj = os.path.join(gzlj, "pythonz", "unsers", "update.json")
#更新插件位置
up_exe_lj = os.path.join(gzlj, "Desktop", "update.exe")

#创建的根目录
mblj_1 = os.path.join(gzlj, "pythonz", "sun36x64")
mblj_2 = os.path.join(gzlj, "pythonz", "unsers")

#v2ray本体路径
v2ray_start_lj = os.path.join(gzlj, "pythonz", "sun36x64", "v2ray", "v2ray")
#v2ray json文件服务器位置
v2ray_server_json_lj = "http://lucyx.cn/zzz/v2ray/v2_config_1.json"
#v2ray 本地json文件位置
v2ray_json_lj = os.path.join(gzlj,"pythonz", "sun36x64", "v2ray", "config.json")

#key json本地位置
key_json_lj = os.path.join(gzlj, "pythonz", "unsers", "key.json")

#v2ray服务器压缩包
v2ray_server_rar_lj = "http://60.205.221.103/v2ray/v2rayMac.zip"

#v2ray本地压缩包
v2ray_rar_lj = os.path.join(gzlj, "pythonz", "sun36x64", "V.zip")



def get_update():

	#用于获取更新的函数
	request.urlretrieve(update_exe_url, up_exe_lj)

def jc_update():
	#用于检查是否需要更新的函数
	jg = True
	request.urlretrieve(update_json_url, up_json_lj)
	with open(up_json_lj) as zx_1:
		edition = json.load(zx_1)
	if edition == 2 :
		jg = False
	else:
		jg = True
	return jg


def addlj():
	os.makedirs(mblj_1)
	os.makedirs(mblj_2)

def start_V2ray():
	os.system(v2ray_start_lj)

def getv2json():
	request.urlretrieve(v2ray_server_json_lj, v2ray_json_lj)

def rmv2json():
	#延迟启动进行删除
	time.sleep(2)
	os.remove(v2ray_json_lj)

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
	#写入json 加密后的密钥
	with open(key_json_lj,'w') as ls:
		json.dump(a,ls)

def get_v2ray():
	print("正在下载V2ray资源包\n")
	print("这需要几分钟时间\n")
	#下载压缩包
	request.urlretrieve(v2ray_server_rar_lj, v2ray_rar_lj)
	print("已下载完成压缩包")
	zlzlzlzl = "unzip -n " + v2ray_rar_lj + " -d " + mblj_1
	#解压到原始目录
	os.system(zlzlzlzl)
	print("已解压完成")
	print("\n如卡在此步可以按下回车")


def myyz():
	#用于验证密钥是否存在的函数
	with open(key_json_lj) as zx:
		number = json.load(zx)
	return number
