# -- coding:utf-8--
import socket
import json
import os
import uuid

#/etc/v2ray/config.json
#service v2ray start
#service v2ray stop

def main():

	js = 0

	while True:
		if js < 1440:
			time.sleep(60)
			js += 1

		else:
			js = 0


def make_uuid():
	new_uid = uuid.uuid4()
	


def change_





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


			#获取配置文件
			elif mod == "config":
				#发送占位符
				pz = get_config()
				cli.sendall(pz.encode())


			#更新配置文件
			elif mod == "upconfig":
				del_config()
				#发送占位符
				cli.sendall("my".encode())
				aaa = cli.recv(2048).decode()
				aaa.split('!')
				#(ip,uuid,port)

				write_config(aaa[0],aaa[1],aaa[2])
				cli.sendall("my".encode())


		except:
			print("e")

if __name__ == "__main__":
	#server()
	print(get_config())





#session.close()


