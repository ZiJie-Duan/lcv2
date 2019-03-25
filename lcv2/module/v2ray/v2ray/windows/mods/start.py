
import json
import os
import time


def wirte_json(server_json):

	gzlj = os.getcwd()
	v2ray_json_lj = r"C:\pythonz5.1\sun36x64\v2ray\config.json"

	json_lb = server_json.split('*')
	ip = json_lb[0]
	port = json_lb[1]
	uid = json_lb[2]


	with open(v2ray_json_lj) as zx:
		userzd = json.load(zx)

	userzd["outbound"]["settings"]["vnext"][0]["address"] = ip
	userzd["outbound"]["settings"]["vnext"][0]["port"] = port
	userzd["outbound"]["settings"]["vnext"][0]["users"][0]["id"] = uid
	userzd["outbound"]["settings"]["vnext"][0]["users"][0]["alterId"] = 100

	with open(v2ray_json_lj,'w') as ojbk_1:
		json.dump(userzd,ojbk_1)

def wirte_json_d():

	gzlj = os.getcwd()
	v2ray_json_lj = r"C:\pythonz5.1\sun36x64\v2ray\config.json"
	
	time.sleep(2)

	with open(v2ray_json_lj) as zx:
		userzd = json.load(zx)

	userzd["outbound"]["settings"]["vnext"][0]["address"] = "000.000.000.000"
	userzd["outbound"]["settings"]["vnext"][0]["port"] = "0000"
	userzd["outbound"]["settings"]["vnext"][0]["users"][0]["id"] = "000000000000000"
	userzd["outbound"]["settings"]["vnext"][0]["users"][0]["alterId"] = 0

	with open(v2ray_json_lj,'w') as ojbk_1:
		json.dump(userzd,ojbk_1)



def start_V2ray():
	gzlj = os.getcwd()
	v2ray_json_lj = r"C:\pythonz5.1\sun36x64\v2ray\v2ray.exe"
	os.system(v2ray_start_lj)

def start_v2(server_json):
	wirte_json(server_json)
	#申请一个子进程开启删除配置文件脚本
	p = multiprocessing.Process(target=wirte_json_d)
	#运行脚本
	p.start()
	#主进程同时打开V2RAY
	start_V2ray()


