# -- coding:utf-8--
import socket
import time
import datetime
import json
import os

def now_time():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx = nowtime.strftime('%Y-%m-%d-%H-%M')
	return timexx

def now_time_show():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx_show = nowtime.strftime('%Y-%m-%d-%H-%M-%S')
	return timexx_show


def wl_time(z):
	#生成未来时间的函数
	nowtime=datetime.datetime.now()
	detaday=datetime.timedelta(days=z)
	da_days=nowtime+detaday
	wltime = da_days.strftime('%Y-%m-%d-%H-%M')
	#输出返回值为 年 月 日 时 分
	return wltime

def userk_username_dzcdq(name):
	yzm = False
	userzclj = "userzc.json"

	with open(userzclj) as zx:
		userdzc = json.load(zx)
	if name in userdzc:
		yzm = True
	else:
		yzm = False

	return yzm



def userk_username_rm(username):
	#用于删除待注册用户名的函数
	userzclj = "userzc.json"

	with open(userzclj) as zx:
		userdzc = json.load(zx)

	userdzc.remove(username) 

	with open(userzclj,'w') as ojbk_1:
		json.dump(userdzc,ojbk_1)


def userk_username_xr_dq(username):
	#用于存储待注册用户名的函数
	userzclj = "userzc.json"

	with open(userzclj) as zx:
		userdzc = json.load(zx)

	userdzc.append(username) 

	with open(userzclj,'w') as ojbk_1:
		json.dump(userdzc,ojbk_1)

def userk_yz_qu():
	#用于取出userk信息的函数
	userklj = "userk.json"
	with open(userklj) as zx:
		userdzc = json.load(zx)
	return userdzc


def userk_username_zc_dq(username):
	#用于读取验证username是否可用的函数
	fh = 0
	userklj = "userk.json"
	with open(userklj) as zx:
		userk = json.load(zx)
	if username in userk.keys():
		fh = 0
	else:
		fh = 1
	return fh


def timeyz(tiz):
	yzjg = False
	timex = now_time()
	if tiz > timex:
		yzjg = True
	else:
		yzjg = False
	return yzjg

def userk_xr(name,password,mac,time):
	#用于添加用户的函数
	userklj = "userk.json"
	with open(userklj) as zx:
		userzd = json.load(zx)
	zhlb = [password, mac, time]

	userzd[name] = zhlb
	with open(userklj,'w') as ojbk_1:
		json.dump(userzd,ojbk_1)


def yzkey_zt(key):
	keyklj = "key.json"
	fhz = 0

	#打开密钥库
	with open(keyklj) as zx:
		keyk = json.load(zx)

	#判断密钥是否在密钥库中
	if key in keyk.keys():
		#获取密钥时间
		keytime = keyk[key]
		#将密钥时间转换为统一格式
		wl_time_sr = wl_time(keytime)
		#删除密钥库中的已用密钥
		del keyk[key]
		#写入到json文件中
		with open(keyklj,'w') as ojbk_1:
			json.dump(keyk,ojbk_1)
		fhz = "1"
		usertime = wl_time_sr
	else:
		#验证时间是否可用
		fhz = "2"
		usertime = "0000-00-00-00-00"

	return fhz, usertime

def key_time_xr(key,username):
	#用于写入时间的函数
	zt, time = yzkey_zt(key)
	if zt == "1":
		userklj = "userk.json"

		with open(userklj) as zx:
			userzd = json.load(zx)

		yhxx = userzd[username]
		yhxx[2] = time

		userzd[username] = yhxx
		with open(userklj,'w') as ojbk_1:
			json.dump(userzd,ojbk_1)


def zczh_zt():
	#用于进行注册的函数
	while True:
		data = cli.recv(2048).decode()
		users_dq = userk_username_zc_dq(data)
		if users_dq == 0:
			#用户名已被注册
			send = "hehehe"
			cli.sendall(send.encode())
		else:
			#用户名没被注册
			send = "trueusername"
			cli.sendall(send.encode())
			userk_username_xr_dq(data)
			break


def dlyz_zt():
	#用于进行登录验证的函数
	ztm = 0
	wuyong = "hahaha"
	#接受用户名
	name = cli.recv(2048).decode()
	cli.sendall(wuyong.encode())
	#接受密码
	password = cli.recv(2048).decode()
	cli.sendall(wuyong.encode())
	#接受mac号
	mac = cli.recv(2048).decode()
	#导入userk
	userk = userk_yz_qu()
	#查询name是否在userk中
	if name in userk.keys():
		user_xx = userk[name]
		#查看密码是否正确
		if password == user_xx[0]:
			time == user_xx[2]
			#查看时间是否有效
			if timeyz(time):
				ztm = 1
			else:
				ztm = 4
		else:
			ztm = 3
	else:
		if userk_username_dzcdq(name):
			time = "0000-00-00-00-00"
			userk_xr(name,password,mac,time)
		else:
			ztm = 2
	#进入回传数据模块		
	if ztm == 1:
		send_hc = "1" + "." + time
		cli.sendall(send_hc.encode())
	if ztm == 2:
		send_hc = "2" + "." + "0000-00-00-00-00"
		cli.sendall(send_hc.encode())
	if ztm == 3:
		send_hc = "3" + "." + "0000-00-00-00-00"
		cli.sendall(send_hc.encode())
	if ztm == 4:
		send_hc = "4" + "." + time
		cli.sendall(send_hc.encode())


















