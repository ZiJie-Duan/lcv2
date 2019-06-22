# -- coding:utf-8--
#this file set place in main server
import socket


def help():
	print("-ak -------- 添加卡密")
	print("-dk -------- 删除卡密")
	print("-lk -------- 浏览卡密")
	print("-lu -------- 浏览用户")
	print("-du -------- 删除用户")
	print("-lc -------- 浏览config")
	print("-dc -------- 删除config")


def add_key():
	print("\n卡密添加模式\n")
	key_name = input("key_name:")
	time = input("time:")
	send_data = key_name + "!" + time

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("root".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall("add-key".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall(send_data.encode())

	fk = sock.recv(1024).decode()

	sock.close()
	print("执行完成，服务器反馈：" + fk)


def del_key():
	print("\n卡密删除模式\n")
	key_name = input("key_name:")
	send_data = key_name

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("root".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall("del-key".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall(send_data.encode())

	fk = sock.recv(1024).decode()

	sock.close()
	print("执行完成，服务器反馈：" + fk)



def skim_key():
	print("\n卡密查询模式\n")

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("root".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall("skim-key".encode())
	server_key = sock.recv(1024).decode()

	sock.close()

	server_key=server_key.split('.')

	for x in server_key:
		print(x)


def skim_user():
	print("\n用户查询模式\n")

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("root".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall("skim-user".encode())
	server_key = sock.recv(1024).decode()

	sock.close()

	server_key=server_key.split('.')

	for x in server_key:
		print(x)


def skim_config():
	print("\n配置查询模式\n")

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("root".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall("skim-config".encode())
	server_key = sock.recv(1024).decode()

	sock.close()

	server_key=server_key.split('.')

	for x in server_key:
		print(x)


def del_user():
	print("\n用户删除模式\n")
	key_name = input("user_name:")
	send_data = key_name

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("root".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall("del-user".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall(send_data.encode())

	fk = sock.recv(1024).decode()

	sock.close()
	print("执行完成，服务器反馈：" + fk)
	

def del_config():
	print("\n配置删除模式\n")
	key_name = input("ip:")
	send_data = key_name

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "192.168.0.11"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("root".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall("del-config".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall(send_data.encode())

	fk = sock.recv(1024).decode()

	sock.close()
	print("执行完成，服务器反馈：" + fk)
	

def mod_c(cs):
	if cs == "-ak":
		add_key()
	if cs == "-dk":
		del_key()
	if cs == "-h":
		help()
	if cs == "-lk":
		skim_key()
	if cs == "-lu":
		skim_user()
	if cs == "-du":
		del_user()
	if cs == "-lc":
		skim_config()
	if cs == "-dc":
		del_config()


def main():
	print("lcv2 后台管理程序 v6.3")
	print(" -h 查看帮助")

	while True:
		cmd = input("lcv2: ")
		mod_c(cmd)

main()