# -- coding:utf-8--
import socket
import threading
import json
import sys
import time

print("证书验证程序")

user_data = []

def init_user_data():
	data = {}
	with open("Sc_data.json",'w') as ojbk:
		json.dump(data,ojbk)

def write_user_data():
	with open("Sc_data.json",'w') as ojbk:
		json.dump(user_data,ojbk)

def read_user_data():
	global user_data
	with open("Sc_data.json") as zx:
		user_data = json.load(zx)
		

def certificate_test():
	global user_data
	while True:
		try:
			host = ""
			port = 5896

			sock = socket.socket()

			sock.bind((host, port))

			sock.listen(5)

			while True:
				print("\n证书验证程序启动！")

				cli, _ = sock.accept()
				print("用户接入接入")

				data = cli.recv(1024).decode()

				print("用户：" + data)
				read_user_data()

				finding_state = False
				for x,_ in user_data.items():
					if x == data:
						finding_state = True

				if finding_state:
					print("证书已找到！发送合法请求！")
					cli.sendall("True".encode())
				else:
					print("证书未找到！发送拒绝请求！")
					cli.sendall("False".encode())

		except Exception as e:
			print(e)
			print("证书服务出错！")

	
def addtra():
	global user_data

	while True:
		try:

			host = ""
			port = 5897

			sock = socket.socket()

			sock.bind((host, port))

			sock.listen(5)

			while True:
				print("\n用户流量结算程序启动！")

				cli, _ = sock.accept()
				print("用户接入接入")

				data = cli.recv(1024).decode()

				data_list = data.split("*data*")
				print("用户：" + data_list[0])
				read_user_data()
				for x,y in user_data.items():
					if x == data_list[0]:
						user_data[x] = y + int(data_list[1])
				
				cli.sendall("Finish".encode())

		except Exception as e:
			print(e)
			print("流量结算服务出错！")
			print("正在重启线程")

def main():
	global user_data

	while True:
		cmd = input(">>")
		cmd = cmd.split(" ")
		if cmd[0] == "au":
			read_user_data()
			user_data[cmd[1]] = 0
			write_user_data()
		elif cmd[0] == "du":
			read_user_data()
			del user_data[cmd[1]]
			write_user_data()

		elif cmd[0] == "ct":
			read_user_data()
			user_data[cmd[1]] = 0
			write_user_data()

		elif cmd[0] == "lu":
			read_user_data()
			for x,y in user_data.items():
				print("用户：" + x +" 流量：" + str(y))

		elif cmd[0] == "init":
			init_user_data()

		elif cmd[0] == "q":
			print("\n退出程序！强制关闭所有守护进程！\n")
			sys.exit()


if __name__=='__main__':
	mainUserUpdatet = threading.Thread(target=addtra)
	mainUserUpdatet.setDaemon(True)
	print("线程1启动！")
	mainUserUpdatet.start()

	mainzs = threading.Thread(target=certificate_test)
	mainzs.setDaemon(True)
	print("线程2启动！")
	mainzs.start()

	while True:
		try:
			print("主核心启动")
			main()
		except Exception as e:
			print(e)
			print("\n核心出错！")
			print("进行全局变量初始化！")
			print("重启核心！\n")


		
