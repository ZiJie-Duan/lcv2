# -- coding:utf-8--
import socket
import time
import datetime
import json
import os

def now_time():
	#内嵌函数
	#用于获取当前时间的函数
	#精确到分钟
	nowtime=datetime.datetime.now()
	timexx = nowtime.strftime('%Y-%m-%d-%H-%M')
	return timexx


def now_time_show():
	#内嵌函数
	#用于获取当前时间的函数
	#精确到秒
	nowtime=datetime.datetime.now()
	timexx_show = nowtime.strftime('%Y-%m-%d-%H-%M-%S')
	return timexx_show


def wl_time(z):
	#内嵌函数
	#生成未来时间的函数
	#参数z为未来要加入的天数
	nowtime=datetime.datetime.now()
	detaday=datetime.timedelta(days=z)
	da_days=nowtime+detaday
	wltime = da_days.strftime('%Y-%m-%d-%H-%M')
	#输出返回值为 年 月 日 时 分
	return wltime


def userk_yz_qu():
	#用于取出userk信息的函数
	userklj = "userk.json"
	with open(userklj) as zx:
		userdzc = json.load(zx)
	return userdzc




















