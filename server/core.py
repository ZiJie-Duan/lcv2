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


def root_control(cmod):

	#用于控制数据库的函数
	if cmod == "add-key":
		#发送占位符
		cli.sendall("my".encode())
		#接受客户端信息请求
		keydata = cli.recv(2048).decode()
		#进行信息分割
		keydata = keydata.split('!')
		#数据结构:key!time
		new_key = Key_data(keyname = keydata[0],keytime = keydata[1])
		# 添加到session:
		session.add(new_user)
		# 提交即保存到数据库:
		session.commit()

		cli.sendall("卡密添加完成！".encode())


	if cmod == "skim-key":
		#用于发送全部卡密的函数
		key_all = session.query(Key_data).all()

		str_key_list = []
		for x in key_all:
			x = str(x)
			str_key_list.append(x)

		send_data = ".".join(str_key_list)

		cli.sendall(send_data.encode())


	if cmod == "skim-user":
		#用于发送全部用户的函数
		user_all = session.query(User_data).all()

		str_user_list = []
		for x in user_all:
			x = str(x)
			str_user_list.append(x)

		send_data = ".".join(str_user_list)

		cli.sendall(send_data.encode())


	if cmod == "skim-config":
		#用于发送全部配置文件的函数
		config_all = session.query(Config_data).all()

		str_config_list = []
		for x in config_all:
			x = str(x)
			str_config_list.append(x)

		send_data = ".".join(str_config_list)

		cli.sendall(send_data.encode())


	if cmod == "del-key":
		#发送占位符
		cli.sendall("my".encode())
		#接受客户端信息请求
		dkey = cli.recv(2048).decode()
		keydata = session.query(Key_data).filter_by(keyname=dkey).first()

		#删除原有卡密
		session.delete(keydata)
		session.commit()

		cli.sendall("卡密删除完成！".encode())


	if cmod == "del-user":
		#发送占位符
		cli.sendall("my".encode())
		#接受客户端信息请求
		duser = cli.recv(2048).decode()
		userdata = session.query(User_data).filter_by(userid=duser).first()

		#删除原有卡密
		session.delete(userdata)
		session.commit()


	if cmod == "del-config":
		#发送占位符
		cli.sendall("my".encode())
		#接受客户端信息请求
		dconfig = cli.recv(2048).decode()
		userdata = session.query(Config_data).filter_by(ip=dconfig).first()

		#删除原有卡密
		session.delete(userdata)
		session.commit()


