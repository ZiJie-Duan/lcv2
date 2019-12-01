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
		+""" reset: false'"""
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

	host = ""
	port = 2233

	sock = socket.socket()

	sock.bind((host, port))

	sock.listen(5)

	while True:

		cli, addr = sock.accept()

		api = Lcv2_api_core()

		data = cli.recv(1024).decode()
		#分割服务指令
		data_list = data.split("*data*")

		if data_list[0] == "add_user":
			api.email = data_list[1]
			api.uuid = data_list[2]
			data = api.api_run()

			if data == "True":
				cli.sendall(data.encode())
			else:
				cli.sendall(data.encode())


		elif data_list[0] == "del_user":
			api.email = data_list[1]
			api.uuid = data_list[2]
			data = api.api_run()

			if data == "True":
				cli.sendall(data.encode())
			else:
				cli.sendall(data.encode())


		elif data_list[0] == "read_user":
			api.email = data_list[1]
			data = api.api_read()

			if type(data) is int :
				data = str(data)
				cli.sendall(data.encode())
			else:
				cli.sendall(data.encode())


		elif data_list[0] == "start_server":






		#cli.sendall(sen.encode())
		#cli.close()















'''

def main():
	#mod 参数为 read / del / add

	mod = input("mod>>")
	email = input("email>>")
	uuidn = str(uuid.uuid4())
	api = Lcv2_api_core()

	if mod == "read":
		api.email = email
		back = api.api_read()
		print(back)

	elif mod == "del":
		api.mod = "del"
		api.uuid = uuidn
		api.email = email
		back = api.api_run()
		print(back)

	elif mod == "add":
		api.mod = "add"
		api.uuid = uuidn
		api.email = email
		back = api.api_run()
		print(back)

main()
'''

