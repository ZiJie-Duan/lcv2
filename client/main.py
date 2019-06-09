# -- coding:utf-8--
import multiprocessing
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import ssl 

from mods import selfprotect,configread,v2raydo,user,server,delold

ssl._create_default_https_context = ssl._create_unverified_context


def main() :
	#主函数

	#获取配置文件
	zbl = configread.return_config()

	#验证是否有更新
	host = zbl["lcv2_server_url"]
	port = zbl["server_port"]
	if selfprotect.check_self_update(host,port):

		if zbl["sys"] == "windows":

			gzlj = os.getcwd()
			uplj = os.path.join(gzlj, "lcv2.zip")

			print("已检测到更新！")
			url = zbl["lcv2_server_install_url"]
			lj = uplj

			input("按下回车开始下载（如速度慢，请重启此程序）")
			#下载更新
			selfprotect.get_update(url,lj)
			print("完成下载更新！")
			print("请手动解压并运行此程序目录下的‘lcv2.zip’")


	else:

		delold.old_rm(zbl["sys"])

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
			
			lj = zbl["lcv2_user_json"]
			if os.path.exists(lj):

				lj = zbl["lcv2_user_json"]
				try:
					userid = user.read_user(lj)
				except:
					print("程序错误！读取用户ID错误！")
					input("按下回车后退出程序！")
					sys.exit(0)

				url = zbl["lcv2_server_url"]
				port = zbl["server_port"]

				if server.login(url,port,userid):
					print("登入成功！")

					url = zbl["lcv2_server_url"]
					lj = zbl["v2rayN_json_bd_lj"]
					v2lj = zbl["v2ray_exe_strat_lj"]
					port = zbl["server_port"]

					try:
						#尝试获取配置
						ipn,uidn,portn = get_config(url,port)
						print("正在开启v2rayN")
						v2raydo.start_V2ray(ipn,uidn,portn,lj,v2lj)
					except:
						print("程序错误！启动v2ray未知错误！")
						input("按下回车后退出程序！")
						sys.exit(0)

					print("程序执行完成！")
					input("请手动关闭此程序！")
					sys.exit(0)

				else:
					print("登入错误！您的密钥不存在或已过期！")
					try:
						print("正在移除卡密")
						rm_lj = zbl["lcv2_user_json"]
						v2raydo.remove_dir(rm_lj)
					except:
						print("程序错误！移除卡密错误！")
						input("按下回车后退出程序！")
						sys.exit(0)
					
					print("若要重新输入请重启程序！")
					input("按下回车后退出程序！")
					sys.exit(0)


			else:
				print("您没有激活程序或程序已过期")
				print("请重新输入密钥！")

				key = input("密钥：")

				url = zbl["lcv2_server_url"]
				port = zbl["server_port"]
				if server.logon(url,port,key):
					print("激活成功！")

					lj = zbl["lcv2_user_json"]

					try:
						user.write_user(lj,key)
					except:
						print("程序错误！写入卡密错误！")
						input("按下回车后退出程序！")
						sys.exit(0)


					url = zbl["lcv2_server_url"]
					lj = zbl["v2rayN_json_bd_lj"]
					v2lj = zbl["v2ray_exe_strat_lj"]
					port = zbl["server_port"]

					try:
						#尝试获取配置
						ipn,uidn,portn = get_config(url,port)
						print("正在开启v2rayN")
						v2raydo.start_V2ray(ipn,uidn,portn,lj,v2lj)
					except:
						print("程序错误！启动v2ray未知错误！")
						input("按下回车后退出程序！")
						sys.exit(0)

					print("程序执行完成！")
					input("请手动关闭此程序！")
					sys.exit(0)

				else:
					print("激活错误！请您检查您的密钥！")
					print("若要重新输入请重启程序！")
					input("按下回车后退出程序！")
					sys.exit(0)


		
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

			syss = zbl["sys"]
			url = zbl["v2ray_server_install_url"]
			ziplj = zbl["v2ray_zip_road"]
			jylj = zbl["v2ray_zip_jy_road"]

			try:
				lj1 = zbl["mkdir_v2ray_lj_1"]
				lj2 = zbl["mkdir_v2ray_lj_2"]
				v2raydo.mkdir_v2lj(lj1,lj2)
			except:
				print("程序错误！创建路径错误！")
				input("按下回车后退出程序！")
				sys.exit(0)

			try:
				input("按下回车开始下载（如速度慢，请重启此程序）")
				v2raydo.get_v2ray(syss,url,ziplj,jylj)
			except:
				print("程序错误！下载v2ray本体错误！")
				input("按下回车后退出程序！")
				sys.exit(0)

			print("程序准备就绪！")
			print("请手动重启程序！")
			input("按下回车后退出程序！")
			sys.exit(0)


		elif zt == 0:

			print("您没有安装v2ray！")
			syss = zbl["sys"]
			url = zbl["v2ray_server_install_url"]
			ziplj = zbl["v2ray_zip_road"]
			jylj = zbl["v2ray_zip_jy_road"]

			try:
				lj1 = zbl["mkdir_v2ray_lj_1"]
				lj2 = zbl["mkdir_v2ray_lj_2"]
				v2raydo.mkdir_v2lj(lj1,lj2)
			except:
				print("程序错误！创建路径错误！")
				input("按下回车后退出程序！")
				sys.exit(0)

			try:
				input("按下回车开始下载（如速度慢，请重启此程序）")
				v2raydo.get_v2ray(syss,url,ziplj,jylj)
			except:
				print("程序错误！下载v2ray本体错误！")
				input("按下回车后退出程序！")
				sys.exit(0)

			print("程序准备就绪！")
			print("请手动重启程序！")
			input("按下回车后退出程序！")
			sys.exit(0)


if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()
	print("lcv2 V6.1")
	main()

