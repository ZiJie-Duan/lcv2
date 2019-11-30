import subprocess


class Lcv2_api_core():
	"""docstring for Lcv2_api_core"""

	def __init__(self,mod,email,uuid):
		self.mod = mod
		self.email = email
		self.uuid = uuid
		self.api_address = "127.0.0.1"
		self.api_port = "10085"
		self.inbound_tag = "main"
		self.level = "1"
		self.alterld = "10"

	def api(self):

		command = "./v2rayapi "+self.mod+" " +\
		self.email+" "+self.uuid+" "+self.api_address\
		+" "+self.api_port+" "+self.inbound_tag\
		+" "+self.level+" "+self.alterld

		back = subprocess.Popen(command, shell=True, \
			stdout=subprocess.PIPE,stderr=\
			subprocess.PIPE).communicate()

		for x in back:
			print(x.decode())


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
		
		