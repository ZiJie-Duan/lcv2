# -- coding:utf-8--
#this file set in the main server
import socket
import time
import datetime
import json
import os

class UserData():
	#用于操作用户数据json的类

	def __init__(self,ip,email,uuid,traffic):
		self.path = "userdata.json"
		self.ip = ip
		self.email = email
		self.uuid = uuid
		self.traffic = traffic
		self.userdata = {}


	def readUserData(self):
		try:
			with open(self.path) as zx:
				userdata = json.load(zx)
				self.userdata = userdata
		except:
			print("\n\nUserData类内部错误！！")
			print("读取用户数据库失败！\n\n")


	def writeUserData(self):
		try:
			with open(self.path,'w') as ojbk:
				json.dump(self.userdata,ojbk)
		except:
			print("\n\nUserData类内部错误！！")
			print("写入用户数据库失败！\n\n")


	def addUser(self):
		try:
			one_user_data_list = [self.email,self.uuid,self.traffic]
			self.userdata[self.ip].append(one_user_data_list)
		except:
			print("\n\nUserData类内部错误！！")
			print("添加用户到指定的ip下失败！\n\n")


	def delUser(self):
		sonserver_users = self.userdata[self.ip]
		
		user_index = 0
		find_state = False
		for one_user_data in sonserver_users:
			if one_user_data[0] == self.email:
				find_state = True
				break
			else:
				user_index += 1

		if find_state :
			del self.userdata[self.ip][user_index]

		else:
			print("\n\nUserData类内部错误！！")
			print("在用户数据库之中没有找到要删除的用户！\n\n")


	def addServer(self):
		try:
			self.userdata[self.ip] = []
		except:
			print("\n\nUserData类内部错误！！")
			print("添加服务器到用户数据库失败！\n\n")


	def delServer(self):
		try:
			del self.userdata[self.ip]
		except:
			print("\n\nUserData类内部错误！！")
			print("删除服务器在用户数据库中失败！\n\n")


	def getUserDetails(self):
		try:
			return self.userdata
		except:
			print("\n\nUserData类内部错误！！")
			print("返回用户信息细节失败！\n\n")


class Lcv2_Socket():

	def __init__(self,ip,email,uuid):
		self.ip = ip
		self.email = email
		self.uuid = uuid
		self.sock = socket.socket()


	def connectServer(self):
		HOST = self.ip
		PORT = 2233
		self.sock.connect((HOST, PORT))
		

	def addLcv2User(self):
		#用于添加用户的函数

		dataList = ["add_user",self.email,self.uuid]
		data = '*data*'.join(dataList)

		self.sock.sendall(data.encode())
		serverRecv = self.sock.recv(1024).decode()

		if serverRecv == "True":
			return True
		else:
			return False


	def delLcv2User(self):
		#用于删除用户的函数

		dataList = ["del_user",self.email,self.uuid]
		data = '*data*'.join(dataList)

		self.sock.sendall(data.encode())
		serverRecv = self.sock.recv(1024).decode()

		if serverRecv == "True":
			return True
		else:
			return False


	def readLcv2User(self):
		#用于读取用户流量使用情况的函数

		dataList = ["read_user",self.email]
		data = '*data*'.join(dataList)

		self.sock.sendall(data.encode())
		serverRecv = self.sock.recv(1024).decode()

		try:
			serverRecv = int(serverRecv)
			return serverRecv
		except:

			return False


	def closeConnect(self):
		self.sock.close()


def initServer(userdata):
	#进行子服务器全部初始化

	for server_ip, users in userdata.items():
		for userOne in users:
			addLcv2User(server_ip,userOne[0],userOne[1])


def mainService():
	
	data = UserData()
	data.readUserData()
	data.getUserDetails()
	
	lcv2Sock = Lcv2_Socket()
	
	for server_ip, users in userdata.items():
		








		
