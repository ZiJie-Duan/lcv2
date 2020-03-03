# -- coding:utf-8--
import socket
import threading

print("证书验证程序")

user_data = []

def zsyz():

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

				finding_state = False
				for x in user_data:
					if x[0] == data:
						finding_state = True
					else:
						finding_state = False

				if finding_state:
					print("证书已找到！发送合法请求！")
					cli.sendall("True".encode())
				else:
					print("证书未找到！发送拒绝请求！")
					cli.sendall("False".encode())
		except:
			print("证书批准服务出错！")
			print("正在重启线程")

def addtra():

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

				js = 0
				for x in user_data:
					if x[0] == data_list[0]:
						user_data[js][1] = x[1] + int(data_list[1])
					js += 1
				
				cli.sendall("Finish".encode())

		except:
			print("流量结算服务出错！")
			print("正在重启线程")

def main():
	while True:
		cmd = input(">>")
		cmd = cmd.split(" ")
		if cmd[0] == "au":
			user_data.append([cmd[1],0])
		elif cmd[0] == "du":
			js = 0
			for x in user_data:
				if x[0] == cmd[1]:
					del user_data[js]
				js += 1

		elif cmd[0] == "ct":
			js = 0
			for x in user_data:
				if x[0] == cmd[1]:
					user_data[0][1] = 0
				js += 1
		elif cmd[0] == "lu":
			for x in user_data:
				print(x)


if __name__=='__main__':
	mainUserUpdatet = threading.Thread(target=addtra)
	mainUserUpdatet.setDaemon(True)
	print("线程1启动！")
	mainUserUpdatet.start()

	mainzs = threading.Thread(target=zsyz)
	mainzs.setDaemon(True)
	print("线程2启动！")
	mainzs.start()

	while True:
		try:
			print("主核心启动")
			main()
		except:
			print("\n核心出错！")
			print("进行全局变量初始化！")
			print("重启核心！\n")

		


		
		
				
