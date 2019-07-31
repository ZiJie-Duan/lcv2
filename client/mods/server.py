# -- coding:utf-8--
import socket
from urllib import request

def login(url,port,user_id):
	'''
	普通连接模式
	需要的数据：
		uuid
	'''
	#开始创建socks
	sock = socket.socket()
	HOST = url
	PORT = port
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("login".encode())
	server_myd = sock.recv(1024).decode()
	#发送id
	sock.sendall(user_id.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()

	if server_s == "F":
		return False
	elif server_s == "T":
		return True


def logon(url,port,user_id):
	'''
	注册连接模式
	需要的数据：
		uuid
	'''
	#开始创建socks
	sock = socket.socket()
	HOST = url
	PORT = port
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("logon".encode())
	server_myd = sock.recv(1024).decode()
	#发送id
	sock.sendall(user_id.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()

	if server_s == "F":
		return False
	elif server_s == "T":
		return True


def get_config(url,port,nu):

	#开始创建socks
	sock = socket.socket()
	HOST = url
	PORT = port
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("config".encode())
	#接受服务器占位符
	server_s = sock.recv(1024).decode()
	#发送数字
	nu = str(nu)
	sock.sendall(nu.encode())
	#接受服务器信息
	server_s = sock.recv(1024).decode()

	sock.close()

	server_s = server_s.split('!')


	return server_s[0],server_s[1],server_s[2]



def get_config_list(url,port):

	#开始创建socks
	sock = socket.socket()
	HOST = url
	PORT = port
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("configlist".encode())
	#接受服务器配置返回值
	server_s = sock.recv(1024).decode()
	sock.close()
	server_s = server_s.split('!')


	return server_s

def xz_server_ip(iplist):
	#让用户进行选择服务器的函数
	#输入服务器列表，判定用户输入是否合法安全
	print("\n\n")
	print("服务器选择模块")

	js = 0
	for x in iplist:
		js += 1
		print(str(js) + ", " + x)

	server = ""

	while True:
		print("")
		server = input("请选择服务器(填写序号)：")
		try:
			server = int(server)

			if server > 0 and server < len(iplist)+1:
				break
			else:
				print("请不要添加空格以及输入非数字字符！")

		except:
			print("请不要添加空格以及输入非数字字符！")

	return server