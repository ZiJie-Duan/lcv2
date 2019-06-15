# -- coding:utf-8--
#this file set place in main server
import os
import socket
import json
import uuid
import time

def change_uuid():

	cc_file = "/etc/v2ray/config.json"
	#cc_file = r"C:\Users\lucycore\Desktop\config.json"

	with open(cc_file,encoding='UTF-8') as zx:
		pzz = json.load(zx)

	uid = str(uuid.uuid4())

	print(uid)

	pzz["inbounds"][0]["settings"]["clients"][0]["id"]\
	= uid
	pzz["inbounds"][0]["port"]\
	= 5000
	pzz["inbounds"][0]["settings"]["clients"][0]["alterId"]\
	= 233


	print("读取完成")

	with open(cc_file,'w') as ojbk:
		json.dump(pzz,ojbk)
	print("写入完成")
	return uid



def send_server(ip,ccss):

	sock = socket.socket()
	#HOST = "www.lucycore.top"
	HOST = "35.229.171.103"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("upconfig".encode())
	server_myd = sock.recv(1024).decode()

	ccss = ip + "!" + ccss + "!" + "5000"
	#发送config
	sock.sendall(ccss.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()

def main():
	ip = input("ip:")
	print("已开启守护程序！")

	js = 0
	while True:
		if js < 1:
			time.sleep(60)
			js += 1

		else:
			js = 0

			os.system("service v2ray stop")
			time.sleep(3)

			uid = change_uuid()

			send_server(ip,uid)
			time.sleep(3)

			os.system("service v2ray start")
			print("已结束进入循环")
main()