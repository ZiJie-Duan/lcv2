# -- coding:utf-8--
import multiprocessing
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import uuid
import ssl 

from mods import install,aess,delold,script,server,start,update,user
#https协议兼容
ssl._create_default_https_context = ssl._create_unverified_context


#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	print("v2ray 启动器V5.1")

	gzlj = os.getcwd()
	#判断是否有更新
	update.update()

	#尝试运行特殊命令
	try :
		script.dtml_srjc()
	except:
		print("")

	#运行旧版本清除模块
	delold.old_rm()

	#判断v2是否安装完整
	if install.t_v2():

		#user文件路径
		userlj = os.path.join(gzlj, "pythonz5.1","unsers","user.json")

		#判断用户文件是否存在
		if os.path.exists(userlj):
			#用户文件存在
			uid = user.read_user()
			print("您的ID：" + uid)
			#连接服务器获取服务器返回值
			ztm, js = server.mod_2(uid)

			#判断服务器是否允许连接
			if ztm == "T":
				#写入json并启动
				start.start_v2(js)

			else:
				user.d_id()
				print("您的账户已过期！正在移除您的账户！")
				print("请您重启此程序！")
				input("按下回车后退出程序！")
				sys.exit()

		else:

			#用户文件不存在
			#生成uuid
			uuid = user.b_id()
			#id格式化
			uuidx = user.uid_cl(uuid)

			print("您的ID：" + uuidx)
			key = input("请输入您的密钥：")

			print("正在验证您的密钥")
			#发送uuid和key至服务器
			ztm, js = server.mod_1(uuid,key)

			#判断服务器是否允许连接
			if ztm == "T":
				print("您的密钥验证通过！")
				#写入用户文件
				user.w_id(uuid)
				#写入配置文件并启动运行
				start.start_v2(js)
			else:
				#验证失败 错误反馈
				print("您的密钥验证失败！")
				print("密钥不存在！")
				print("请您重启此程序！并重新输入！")
				input("按下回车后 关闭程序！")
				sys.exit()

	else:
		#删除v2文件目录
		install.del_v2()
		#创建路径
		install.addlj()
		#下载安装v2本体
		install.get_v2ray()
		print("请您重启此程序！")
		input("按下回车后 关闭程序！")
		sys.exit()
		









