# -- coding:utf-8--
#this file set place in main server
import socket


def help():
	print("\n\n")
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
	HOST = "www.lucycore.top"
	#HOST = "35.229.171.103"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
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
	HOST = "www.lucycore.top"
	#HOST = "35.229.171.103"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("del-key".encode())
	server_myd = sock.recv(1024).decode()

	sock.sendall(send_data.encode())

	fk = sock.recv(1024).decode()

	sock.close()
	print("执行完成，服务器反馈：" + fk)



def mod_c(cs):
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":
	if cs == "":


def main():
	print("lcv2 后台管理程序 v6.3")
	print(" -h 查看帮助")

	while True:
		cmd = input("lcv2: ")
		mod_c(cmd)


