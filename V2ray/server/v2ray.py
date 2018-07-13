# -- coding:utf-8--
import socket
import time
import datetime
import json
import os
import mods

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

print("v2ray server start！")

while True:
    try:
        #堵塞连接
        cli, addr = sock.accept()
        #打印连接pi及信息
        show_time = mods.now_time_show()
        print("")
        print(addr)
        print(show_time)
        #接收模式识别码
        data = cli.recv(2048).decode()
        cli.sendall("...".encode())
        #验证密钥
        if data == "key":
            #接受名称
            name = cli.recv(2048).decode()
            cli.sendall("...".encode())
            #接受密钥
            key = cli.recv(2048).decode()
            cli.sendall("...".encode())
            key_time_xr(key,name)
        if data == "zc":
            zczh_zt()
        if data == "dl":
            dlyz_zt()


        print("")
        #关闭连接
        cli.close()
    except:
        show_time = mods.now_time_show()
        print("\n错误！")
        print(show_time)
        print("\n")