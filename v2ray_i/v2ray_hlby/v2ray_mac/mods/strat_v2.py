# -- coding:utf-8--
import multiprocessing
import json
import os
from urllib import request

#工作路径
gzlj = os.getcwd()

#v2ray json文件服务器位置
v2ray_server_json_lj = "http://www.lucycore.top/zzz/v2ray/v2_config_hlby.json"

v2ray_json_lj = os.path.join(gzlj,"pythonz5","sun36x64","v2ray","config.json")
#v2ray本体路径
v2ray_start_lj = os.path.join(gzlj,"pythonz5","sun36x64","v2ray","v2ray")

def getv2json():
	request.urlretrieve(v2ray_server_json_lj, v2ray_json_lj)

def start_V2ray():
	os.system(v2ray_start_lj)

def start_v2():
	try:
		print("正在尝试获取配置文件\n")
		getv2json()
		print("获取配置文件成功！\n")
	except:
		print("获取配置文件失败！\n")
		print("正在使用本地配置连接！\n")

	#主进程同时打开V2RAY
	start_V2ray()