# -- coding:utf-8--
import socket
import time
import datetime
import json
import os


def future_time(day):
	#生成未来时间的函数
	nowtime=datetime.datetime.now()
	detaday=datetime.timedelta(days=day)
	da_days=nowtime+detaday
	wltime = da_days.strftime('%Y-%m-%d-%H-%M')
	#输出返回值为 年 月 日 时 分
	return wltime


def now_time():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx = nowtime.strftime('%Y-%m-%d-%H-%M')
	return timexx
	

def yz_time(fu):
	#验证时间是否合法的函数

	timex = now_time()

	if fu > timex:
		return True
	else:
		return False

