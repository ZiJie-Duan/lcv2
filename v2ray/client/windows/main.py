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

from mods import install_v2,lod_del,tool_win,update,lod_del,user,s_server,X,strat_v2

ssl._create_default_https_context = ssl._create_unverified_context

def strat():
	#检测更新
	update.update()
	#检测是否正确安装v2ray
	if install_v2.t_v2():
		#检测时候有保存uuid
		zt, user_id = user.test_user_f()
		if zt:
			#发送uuid进行验证
			sr_re,sr_time,sr_json,sr_gg,sr_x = s_server.mod_1(user_id)
			#是否允许连接
			if sr_re:
				#发布日志
				X.gg(sr_gg)
				X.dtml_srjc(sr_x)
				#启动程序
				strat_v2.start_v2(sr_json)
			else:
				#延长时间模式
				s_server.mod_2(user_id)
				strat()
		else:
			#生成uuid并写入
			user.write_user_id()
			#进行注册
			s_server.mod_3(user_id)
			strat()
			
	else:
		print("您没有安装或没有正确安装v2ray!")
		try:
			#删除文件的函数
			install_v2.d_v2_s()
			print("正在重新安装v2")
			#创建路径的函数
			install_v2.addlj()
			#安装v2的函数
			install_v2.get_v2ray()
			strat()
		except:
			print("正在安装v2")
			#创建路径的函数
			install_v2.addlj()
			#安装v2的函数
			install_v2.get_v2ray()
			strat()


strat()