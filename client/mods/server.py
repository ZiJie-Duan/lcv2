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
