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

from mods import selfprotect,configread,v2raydo

ssl._create_default_https_context = ssl._create_unverified_context


def main() :
	#主函数

	#获取配置文件
	zbl = configread.return_config()

	#验证是否有更新
	host = zbl["lcv2_update_url"]
	if selfprotect.check_self_update(host):

		print("已检测到更新！")
		url = zbl["lcv2_server_install_url"]
		lj = zbl["lcv2_zip_bd_lj"]

		input("按下回车开始下载更新")
		#下载更新
		selfprotect.get_update(url,lj)
		print("完成下载更新！")
		print("请手动解压‘’")

	else:
		zt = 0 
		#zt=0 代表从未安装v2 zt=1安装却不完整
		#zt=2 安装完整
		#用于分辨状态的函数
		lj = zbl["mkdir_v2ray_lj_1"]
		if os.path.exists(lj):
			try:
				lj = zbl["mkdir_v2ray_lj_1"]
				yzlist = zbl["v2ray_bt_yz_list"]
				if v2raydo.test_v2_ins(lj,yzlist):
					zt = 2
				else:
					zt =1
			except:
				zt = 0
		else:
			zt = 0



		if zt == 2:
			print("ok")
		
		elif zt == 1:
			print("检测到您的v2ray文件不完整！")
			print("准备进行重新安装！")

			try:
				print("正在删除v2ray本体")
				rm_lj = zbl["v2ray_rm_all"]

				v2raydo.remove_dir(rm_lj)

			except:
				print("程序错误！移除v2ray本体错误！")
				input("按下回车后退出程序！")
				sys.exit(0)

			sys = zbl["sys"]
			url = zbl["v2ray_server_install_url"]
			ziplj = zbl["v2ray_zip_road"]
			jylj = zbl["v2ray_zip_jy_road"]

			try:
				get_v2ray(sys,url,ziplj,jylj)
			except:
				print("程序错误！下载v2ray本体错误！")
				input("按下回车后退出程序！")
				sys.exit(0)


		elif zt == 0:

			print("您没有安装v2ray！")
			sys = zbl["sys"]
			url = zbl["v2ray_server_install_url"]
			ziplj = zbl["v2ray_zip_road"]
			jylj = zbl["v2ray_zip_jy_road"]

			try:
				get_v2ray(sys,url,ziplj,jylj)
			except:
				print("程序错误！下载v2ray本体错误！")
				input("按下回车后退出程序！")
				sys.exit(0)

		


main()


