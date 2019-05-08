import socket
from urllib import request

def mod_1(user_id):
	'''
	普通连接模式
	需要的数据：
		uuid
	服务器命令分割：
		re -> 是否允许连接
		time -> 时间 到期时间
		json -> v2服务器配置文件
		gg -> 服务器公告
	'''
	#开始创建socks
	sock = socket.socket()
	HOST = "192.168.1.104"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("mod_1".encode())
	server_myd = sock.recv(1024).decode()
	#发送id
	sock.sendall(user_id.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()
	#服务器命令分割
	sr_lb = server_s.split('.')
	sr_re = sr_lb[0]
	sr_time = sr_lb[1]
	sr_json = sr_lb[2]
	sr_gg = sr_lb[3]
	sr_x = sr_lb[4]

	return sr_re,sr_time,sr_json,sr_gg,sr_x


def mod_2(user_id):
	'''
	密钥添加模式
	需要的数据：
		uuid, key
	服务器命令分割：
		re -> 是否激活成功
	'''
	print("您还没有激活 或 已到期！")
	print("请重新输入密钥激活程序！")
	key = input("请输入密钥：")
	while key == "":
		print("不可以输入空白内容！")
		key = input("请输入密钥：")

	#开始创建socks
	sock = socket.socket()
	HOST = "192.168.1.104"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("mod_2".encode())
	server_myd = sock.recv(1024).decode()
	#发送id
	sock.sendall(user_id.encode())
	server_myd = sock.recv(1024).decode()
	#发送key
	sock.sendall(user_id.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()
	#服务器命令分割
	if server_s == "True":
		print("激活成功！")
		print("正在重启程序！")
	else:
		print("激活失败！")
		print("请重新输入密钥！")
		mod_2(user_id)

	

def mod_3(user_id):
	'''
	注册模式
	需要的数据：
		uuid
	服务器命令分割：
		re -> 是否注册成功
	'''
	#开始创建socks
	sock = socket.socket()
	HOST = "192.168.1.104"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("mod_3".encode())
	server_myd = sock.recv(1024).decode()
	#发送id
	sock.sendall(user_id.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()
	#服务器命令分割
	sr_re = server_s
	
	if sr_re == "True":
		print("注册成功！")
	else:
		mod_3(user_id)