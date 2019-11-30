#!/usr/bin/env python
# coding: utf-8
# author: Xiao Guaishou
import os

try:
    import psutil
except ImportError:
    print('Error: psutil module not found!')
    exit()


def kill():
	a = psutil.pids()
	for x in a:
		p = psutil.Process(x)
		b = p.name()
		if b == "v2ray.exe":
			print("进程号：" + str(x))
			#os.system("taskkill /f /im v2ray.exe")


def get_wifi():
	net = psutil.net_io_counters()  
	bytes_sent = round(net.bytes_sent / 1024,2)
	bytes_rcvd = round(net.bytes_recv / 1024,2)

	bytes_sentx = round(int(bytes_sent) / 1024,3)
	bytes_rcvdx = round(int(bytes_rcvd) / 1024,3)

	#bytes_sent = '{0:.2f} kb'.format(net.bytes_recv / 1024)  
	#bytes_rcvd = '{0:.2f} kb'.format(net.bytes_sent / 1024) 
	print(u"网卡接收流量 %smb 网卡发送流量 %smb"%(bytes_rcvdx, bytes_sentx)) 


while True:
	get_wifi()
	input()