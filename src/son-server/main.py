import subprocess
import uuid
import socket
import time
import re


class Lcv2_api_core():
	"""docstring for Lcv2_api_core
	用于操作v2ray api工具的子服务器控制模块
	包含有以下 api 功能：
		添加用户
		删除用户
		读取用户流量使用情况
	以上所有功能的实现必须提供邮箱与uuid
	"""

	def __init__(self,mod="",email="",uuid=""):
		self.mod = mod
		self.email = email
		self.uuid = uuid
		self.api_address = "127.0.0.1"
		self.api_port = "10085"
		self.inbound_tag = "main"
		self.level = "0"
		self.alterld = "10"


	def api_run(self):

		command = "./v2rayapi "+self.mod+" " +\
		self.email+" "+self.uuid+" "+self.api_address\
		+" "+self.api_port+" "+self.inbound_tag\
		+" "+self.level+" "+self.alterld
		print(command)
		back = subprocess.Popen(command, shell=True, \
			stdout=subprocess.PIPE,stderr=\
			subprocess.PIPE).communicate()


		alist = []
		for x in back:
			alist.append(x.decode())

		data = alist[1].split(" ")
		data = data[2]

		if data == "ok:":
			return "True"
		else:
			alist = "*data*".join(alist)
			return alist
		#此函数返回值 如果是正确的内容
		#将返回Ture字符串，否则将返回错误string


	def api_read(self):

		command = "/usr/bin/v2ray/v2ctl api --server=" + self.api_address\
		+":"+self.api_port+""" StatsService.GetStats 'name: """\
		+'"user>>>'+self.email+'>>>traffic>>>downlink" '\
		+""" reset: true'"""
		print(command)
		back = subprocess.Popen(command, shell=True, \
			stdout=subprocess.PIPE,stderr=\
			subprocess.PIPE).communicate()


		alist = []
		for x in back:
			alist.append(x.decode())

		try:

			data = alist[0].split("  ")
			data = data[2]
			data = re.sub(r"\D", "", data)
			data = int(data)
			data = data//1048576
			#返回值直接换算为mb单位
			return data

		except:

			alist = "*data*".join(alist)
			return alist
		#此函数返回值 如果是正确的内容
		#将返回int类型的数字，否则将返回错误string



def main():
	print("声明套接字主机")

	host = ""
	port = 2233

	sock = socket.socket()

	sock.bind((host, port))

	sock.listen(5)

	while True:

		print("\n开始监听！")

		cli, addr = sock.accept()
		print("操作端接入")

		api = Lcv2_api_core()

		data = cli.recv(1024).decode()
		#分割服务指令
		data_list = data.split("*data*")

		if data_list[0] == "read_user":
			#匹配服务器为测试用户流量是否合法
			print("读取用户流量模式")
			api.email = data_list[1]
			data = api.api_read()

			if type(data) is int :
				data = str(data)
				cli.sendall(data.encode())
				print("用户流量读取完成！")
				print("流量：" + data)
			else:
				cli.sendall(data.encode())
				print("用户流量读取错误！")
				print("\n" + data + "\n")
				print("以上为错误反馈！")


		elif data_list[0] == "add_user":
			#匹配服务器为增加删除用户模式
			print("添加用户模式")
			api.mod = "add"
			api.email = data_list[1]
			api.uuid = data_list[2]
			data = api.api_run()

			if data == "True":
				cli.sendall("True".encode())
				print("添加用户完成！")
			else:
				cli.sendall(data.encode())
				print("添加用户错误！")
				print("\n" + data + "\n")
				print("以上为错误反馈！")


		elif data_list[0] == "del_user":
			#匹配服务器为增加删除用户模式
			print("删除用户模式")
			api.mod = "del"
			api.email = data_list[1]
			api.uuid = data_list[2]
			data = api.api_run()

			if data == "True":
				cli.sendall("True".encode())
				print("删除用户完成！")
			else:
				cli.sendall(data.encode())
				print("删除用户错误！")
				print("\n" + data + "\n")
				print("以上为错误反馈！")

		print("完成一次调用！")


if __name__=='__main__':
	print("Lcv2 V7.0 子服务器 启动")

	while True:
		try:
			print("主核心启动")
			main()
		except:
			print("\n核心出错！")
			print("进行全局变量初始化！")
			print("重启核心！\n")

