# -- coding:utf-8--
import socket
import time
import datetime
import json
import os
import core
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

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



def write_config(ip,uuid,port):
	#写入config的函数
	pz = Config_data(ip=ip,uuid=uuid,port=port)
	session.add(pz)
	session.commit()

def del_config(ip):
	#获取ip的函数
	aa = session.query(Config_data)\
	.filter_by(ip=ip).first()
	#删除原有卡密
	session.delete(aa)
	session.commit()

#////////////////////////////////////////////
def get_config():
	a = Config_data(ip="111",uuid="qwsazx",port="2202")
	session.add(a)
	session.commit()
	#获取ip的函数
	aa = session.query(Config_data).all()
	#删除原有卡密
	aa = str(aa)
	return aa


def test_key(key):
	#验证卡密是否存在的函数
	a = session.query(Key_data).first()
	a = str(a)

	if a is not None:
		return True
	else:
		return False


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

			#接收模式识别
			mod = cli.recv(2048).decode()

			#模式为验证更新
			if mod == "update":
				#发送程序版本
				cli.sendall("6.1".encode())


			#模式为登陆模式
			elif mod == "login":
				#发送占位
				cli.sendall("my".encode())
				#接收用户id
				userid = cli.recv(2048).decode()
				#验证用户时间是否合法
				if yz_userid(userid):
					cli.sendall("T".encode())
				else:
					cli.sendall("F".encode())


			#模式为注册模式
			elif mod == "logon":
				#发送占位符
				cli.sendall("my".encode())
				#接收密钥
				key = cli.recv(2048).decode()
				#测试密钥是否存在
				if test_key(key):
					#获取密钥时间并转换
					ft = get_key(key)
					write_userid(key,ft,"0000")
					cli.sendall("T".encode())
					
				else:
					cli.sendall("F".encode())



		except:
			print("e")

if __name__ == "__main__":
	#server()
	print(get_config())





#session.close()


