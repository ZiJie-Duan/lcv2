# -- coding:utf-8--
import socket



#声明主机
host = ""
#声明端口号
port = 2333
#创建sock套接字
sock = socket.socket()
#绑定主机和端口
sock.bind((host, port))
#开始监听
sock.listen(5)
#对话循环

print("v2ray core port start!")

while True:
	try:
		#堵塞连接
		cli, addr = sock.accept()
		#接收模式识别
		mod = cli.recv(2048).decode()

		if mod == "core":
			print(addr)
			print("通过内部端口启动\n")
			cli.sendall("go".encode())
		else:
			cli.sendall("F".encode())

		#关闭连接
		cli.close()
	except:

		print("\n错误！")

		print("\n") 