# -- coding:utf-8--
import socket
from urllib import request

def yz():
	'''
	请求接入
	'''
	#开始创建socks
	sock = socket.socket()
	HOST = '60.205.221.103'
	PORT = 2333
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("core".encode())
	servers = sock.recv(1024).decode()
	
	if servers == "go":
		re = True
	else:
		re = False

	return re



