import json
import os

def userk_xr(uuid):
	#用于添加用户的函数
	root = False
	x = "0"
	time = "0000"

	userklj = "userk.json"

	with open(userklj) as zx:
		userzd = json.load(zx)

	zhlb = [time,root,"0","0",x]

	userzd[uuid] = zhlb

	with open(userklj,'w') as ojbk_1:
		json.dump(userzd,ojbk_1)


def time_tjkey(uuid,time):
	#用于延长卡密时间
	fhz = True
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)

	user_xx = userk[uuid]
	user_xx[0] = time
	userk[uuid] = user_xx
	#写入到json文件中
	with open(userklj,'w') as ojbk_1:
		json.dump(userk,ojbk_1)


