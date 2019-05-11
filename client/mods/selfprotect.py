# -- coding:utf-8--
from urllib import request
import socket
import os


def Schedule(a,b,c):
	#显示进度的函数
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
	print('%.2f%%' %(per))


def check_self_update(host,port):
	#返回true or false
	#用于检查是否需要更新的函数
	update_bb = "6.0"
	sock = socket.socket()
	HOST = host
	PORT = port
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("update".encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()

	if server_s == update_bb:
		return False
	else:
		return True


def get_update(url,lj):
	#用于获取更新的函数
	request.urlretrieve(url, lj, Schedule)


