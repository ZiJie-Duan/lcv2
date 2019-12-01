import subprocess
import uuid

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
		self.level = "1"
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

		return alist


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

		return alist


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