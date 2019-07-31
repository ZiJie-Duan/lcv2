# -- coding:utf-8--
#this file set place in main server
import socket
import time
import datetime
import json
import os
import core
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import random

# 创建对象的基类:
Base = declarative_base()

# 定义Key对象:
class Key_data(Base):
    # 表的名字:
    __tablename__ = 'keys'

    # 表的结构:
    keyname = Column(String(50),unique=True,primary_key=True)
    keytime = Column(String(10))

    def __repr__(self):

        return "{name}!{time}".format(name=self.keyname\
            ,time=self.keytime)


# 定义User对象:
class User_data(Base):
    # 表的名字:
    __tablename__ = 'users'

    # 表的结构:
    userid = Column(String(50),unique=True,primary_key=True)
    due = Column(String(20))
    otime = Column(String(20))

    def __repr__(self):

        return "{userid}!{due}!{otime}".format(userid=self.userid\
            ,due=self.due,otime=self.otime)


# 定义User对象:
class Config_data(Base):
    # 表的名字:
    __tablename__ = 'config'

    # 表的结构:
    ip = Column(String(50),unique=True,primary_key=True)
    uuid = Column(String(20))
    port = Column(String(20))

    def __repr__(self):

        return "{ip}!{uuid}!{port}".format(ip=self.ip\
            ,uuid=self.uuid,port=self.port)



# 初始化数据库连接:
engine = create_engine('sqlite:///test.db')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

# 创建session对象:
session = DBSession()



def cheak_user_out():
	#用于回收数据库无用资源的函数
	aa = session.query(User_data).all()

	for x in aa:
		a = str(x).split('!')

		if core.yz_time(a[1]) == False:

			session.delete(x)
			session.commit()


def write_config(ip,uuid,port):
	#写入config的函数
	pz = Config_data(ip=ip,uuid=uuid,port=port)
	session.add(pz)
	session.commit()


def test_config(ip):
	#验证config是否存在相同ip的项目
	aa = session.query(Config_data)\
	.filter_by(ip=ip).first()

	if aa is not None:

		session.delete(aa)
		session.commit()
		return True

	else:
		return False


def get_config_list():
	#获取ip的函数
	
	aa = session.query(Config_data).all()

	iplist = []
	for x in aa:
		x = str(x)
		x = x.split('!')[0]
		iplist.append(x)

	ret = "!".join(iplist)


	return aa



def get_config(z):
	#获取ip的函数
	aa = session.query(Config_data).all()

	aa = aa[z]
	aa = str(aa)
	#此时aa是一个列表

	return aa


def get_key(key):
	#获取卡密的函数
	aa = session.query(Key_data)\
	.filter_by(keyname=key).first()
	#分割返回值
	a = str(aa).split('!')
	#生成未来时间
	ft = core.future_time(int(a[1]))
	#删除原有卡密
	session.delete(aa)
	session.commit()

	return ft


def write_userid(userid,due,otime):
	#写入用户信息的函数
	userd = User_data(userid=userid,due=due,otime=otime)
	session.add(userd)
	session.commit()


def yz_userid(userid):
	#验证用户是否可用的函数
	aa = session.query(User_data)\
	.filter_by(userid=userid).first()

	if aa is not None:
		a = str(aa).split('!')

		if core.yz_time(a[1]):
			return True

		else:
			return False

	else:
		return False



def server():

	#声明主机
	host = ""
	#声明端口号
	port = 2233
	#创建sock套接字
	sock = socket.socket()
	#绑定主机和端口
	sock.bind((host, port))
	#开始监听
	sock.listen(5)
	#对话循环

	print("v2ray server start！")

	while True:
		try:
			#堵塞连接
			cli, addr = sock.accept()
			print("\n\n客户端接入！")
			print(addr)

			#接收模式识别
			mod = cli.recv(2048).decode()

			#模式为验证更新
			if mod == "update":
				print("验证更新！")
				#发送程序版本
				cli.sendall("6.2".encode())


			#模式为登陆模式
			elif mod == "login":
				print("登陆验证！")
				#发送占位
				cli.sendall("my".encode())
				#接收用户id
				userid = cli.recv(2048).decode()
				#验证用户时间是否合法
				if yz_userid(userid):
					print("验证通过！")
					cli.sendall("T".encode())
				else:
					print("验证拒绝！")
					cli.sendall("F".encode())


			#模式为注册模式
			elif mod == "logon":
				print("注册验证！")
				#发送占位符
				cli.sendall("my".encode())
				#接收密钥
				key = cli.recv(2048).decode()
				#尝试从服务器中获取key
				try:
					#获取密钥时间并转换
					ft = get_key(key)
					write_userid(key,ft,"0000")
					cli.sendall("T".encode())
					print("验证通过！")
				except:
					print("验证拒绝！")
					cli.sendall("F".encode())


			#获取配置文件列表
			elif mod == "configlist":
				print("配置列表发送")
				#发送占位符
				pz = get_config_list()
				cli.sendall(pz.encode())



			#获取配置文件
			elif mod == "config":
				print("配置发送")
				#发送占位符
				pz = get_config()
				cli.sendall(pz.encode())


			#更新配置文件
			elif mod == "upconfig":
				print("配置更新！")
				#发送占位符
				cli.sendall("my".encode())
				configs = cli.recv(2048).decode()
				cli.sendall("ok".encode())
				configs = configs.split('!')
				#(ip,uuid,port)

				if test_config(configs[0]):

					write_config(configs[0],configs[1],configs[2])

				else:

					write_config(configs[0],configs[1],configs[2])

				cheak_user_out()


			#管理程序操作模式
			elif mod == "root":
				print("管理操作模式")
				#发送占位符
				cli.sendall("my".encode())
				cmod = cli.recv(2048).decode()

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
					session.add(new_key)
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
					cli.sendall("用户删除完成！".encode())


				if cmod == "del-config":
					#发送占位符
					cli.sendall("my".encode())
					#接受客户端信息请求
					dconfig = cli.recv(2048).decode()
					userdata = session.query(Config_data).filter_by(ip=dconfig).first()

					#删除原有卡密
					session.delete(userdata)
					session.commit()
					cli.sendall("配置删除完成！".encode())


		except:
			print("\n\n发生未知错误！\n\n")


if __name__ == "__main__":
	print("lcv2 V6.3")
	server()



#session.close()


