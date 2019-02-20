import socket
from urllib import request
 


def mod_2(uuid):
	'''
	普通模式
	需要的数据：
		uuid
	服务器命令分割：
		re -> 是否激活成功
	'''

	#开始创建socks
	sock = socket.socket()
	HOST = '10.10.1.58'
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("mod_2".encode())
	server_myd = sock.recv(1024).decode()
	#发送id
	sock.sendall(uuid.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	#服务器命令分割
	if server_s == "ok":
		#获取配置文件
		sock.sendall("my".encode())
		server_json = sock.recv(1024).decode()
		sock.close()
		return "T", server_json
	else:
		sock.close()
		return "F", "00*00*00"
		

	

def mod_1(uuidx,key):
	'''
	注册模式
	需要的数据：
		uuid & key
	服务器命令分割：
		re -> 是否注册成功
	'''
	#开始创建socks
	sock = socket.socket()
	HOST = '10.10.1.58'
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("mod_1".encode())
	server_myd = sock.recv(1024).decode()
	#发送uuid
	sock.sendall(str(uuidx).encode())
	server_myd = sock.recv(1024).decode()
	#发送key
	sock.sendall(key.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()

	if server_s == "ok":
		sock.sendall("my".encode())
		server_json = sock.recv(1024).decode()
		sock.close()
		return "T", server_json
	else:
		return "F", "00*00*00"
		sock.close()
	
	





