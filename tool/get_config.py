# -- coding:utf-8--
import multiprocessing
import os
import json
import socket
import ssl


ssl._create_default_https_context = ssl._create_unverified_context



if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	print("lcv2 MacOS V6.2")

	update_bb = "6.3"
	sock = socket.socket()
	HOST = "www.lucycore.top"
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("update".encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	#发送模式
	sock.close()
	
	if server_s == update_bb:
		print("版本验证成功！")
		gzlj = os.getcwd()

		sock = socket.socket()
		sock.connect((HOST, PORT))
		sock.sendall("config".encode())
		server_s = sock.recv(1024).decode()
		sock.sendall("1".encode())
		#接受服务器的状态码
		server_s = sock.recv(1024).decode()
		server_s = server_s.split('!')
		print(server_s)
		'''
		mb_lj = gzlj + "/v2ray/config.json"
		with open(mb_lj,encoding='UTF-8') as zx:
			pzz = json.load(zx)

		pzz["outbounds"][0]["settings"]["vnext"][0]["address"] = server_s[0]
		pzz["outbounds"][0]["settings"]["vnext"][0]["port"] = server_s[2]
		pzz["outbounds"][0]["settings"]["vnext"][0]["users"][0]["id"] = server_s[1]

		with open(mb_lj,'w') as ojbk:
			json.dump(pzz,ojbk)

		print("配置写入完成！")
		print("按下回车关闭此程序")
		'''
		
	else:
		print("此版本已过期！请点击链接下载最新版本！")
		print("http://www.lucycore.top/v2ray/lcv2Mac.zip")
		input("按下回车后退出！")
		sys.exit(0)





'''
	numbers = [1,2,3,4,5,6,7,8,9]
	filename = 'numbers.json'
	with open(filename,'w') as ojbk:
		json.dump(numbers,ojbk)

	with open(filename) as zx:
		number = json.load(zx)

'''


		

	
