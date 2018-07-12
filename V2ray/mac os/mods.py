# -- coding:utf-8--
from su.aes import encrypt, decrypt
import multiprocessing
from urllib import request
import mods
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import uuid

keytxt = "LucycoreX"

#工作路径
gzlj = os.getcwd()
#是否有更新验证文件位置
update_json_url = "http://lucyx.cn/zzz/v2ray/update.json"
#服务器更新文件位置
update_exe_url = "http://60.205.221.103/v2ray/updateformac"
#更新验证文件位置
up_json_lj = os.path.join(gzlj, "pythonz3", "unsers", "update.json")
#更新插件位置
up_exe_lj = os.path.join(gzlj, "Desktop", "更新v2ray")

#创建的根目录
mblj_1 = os.path.join(gzlj, "pythonz3", "sun36x64")
mblj_2 = os.path.join(gzlj, "pythonz3", "unsers")

#v2ray本体路径
v2ray_start_lj = os.path.join(gzlj, "pythonz3", "sun36x64", "v2ray", "v2ray")
#v2ray json文件服务器位置
v2ray_server_json_lj = "http://lucyx.cn/zzz/v2ray/v2_config_1.json"
#v2ray 本地json文件位置
v2ray_json_lj = os.path.join(gzlj,"pythonz3", "sun36x64", "v2ray", "config.json")

#key json本地位置
user_json_lj = os.path.join(gzlj, "pythonz3", "unsers", "user.json")

#v2ray服务器压缩包
v2ray_server_rar_lj = "http://60.205.221.103/v2ray/v2rayMac.zip"

#v2ray本地压缩包
v2ray_rar_lj = os.path.join(gzlj, "pythonz3", "sun36x64", "V.zip")

#用户偏好设置文件
user_phsz_json_lj = os.path.join(gzlj, "pythonz3", "unsers", "Preference.json")

def user_preference():
	#用于验证用户偏好设置的函数
	with open(user_phsz_json_lj) as zx:
		number = json.load(zx)
	return number


def aes_a(key,text):
	#加密函数
	mw = encrypt(key, text)
	return mw

def aes_b(key,mw):
	#解密函数
	mw = decrypt(key, mw)
	return mw

def get_MAC():
	#获取Mac的函数
	mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
	return ":".join([mac[e:e+2] for e in range(0,11,2)])


def get_update():

	#用于获取更新的函数
	request.urlretrieve(update_exe_url, up_exe_lj)

def jc_update():
	#用于检查是否需要更新的函数
	jg = True
	request.urlretrieve(update_json_url, up_json_lj)
	with open(up_json_lj) as zx_1:
		edition = json.load(zx_1)
	if edition == 2 :
		jg = False
	else:
		jg = True
	return jg


def addlj():
	#创建路径的函数
	os.makedirs(mblj_1)
	os.makedirs(mblj_2)

def start_V2ray():
	os.system(v2ray_start_lj)

def getv2json():
	request.urlretrieve(v2ray_server_json_lj, v2ray_json_lj)

def rmv2json():
	#延迟启动进行删除
	time.sleep(2)
	os.remove(v2ray_json_lj)

def remove_dir(dir):
	#用于删除路径的函数
	dir = dir.replace('\\', '/')
	if(os.path.isdir(dir)):
		for p in os.listdir(dir):
			remove_dir(os.path.join(dir,p))
		if(os.path.exists(dir)):
			os.rmdir(dir)
	else:
		if(os.path.exists(dir)):
			os.remove(dir)


def now_time():
	#用于获取当前时间的函数
	nowtime=datetime.datetime.now()
	timexx = nowtime.strftime('%Y-%m-%d-%H-%M')
	return timexx


def wl_time(z):
	#生成未来时间的函数
	nowtime=datetime.datetime.now()
	detaday=datetime.timedelta(days=z)
	da_days=nowtime+detaday
	wltime = da_days.strftime('%Y-%m-%d-%H-%M')
	#输出返回值为 年 月 日 时 分
	return wltime

def put_phsz(a):
	#用于输出用户个人偏好文件的函数
	with open(user_phsz_json_lj,'w') as ls:
		json.dump(a,ls)

def put_key(a):
	#用于输出用户信息文件的函数
	#写入json 加密后的信息
	with open(key_json_lj,'w') as ls:
		json.dump(a,ls)

def get_v2ray():
	print("正在下载V2ray资源包\n")
	print("这需要几分钟时间\n")
	#下载压缩包
	request.urlretrieve(v2ray_server_rar_lj, v2ray_rar_lj)
	print("已下载完成压缩包")
	zlzlzlzl = "unzip -n " + v2ray_rar_lj + " -d " + mblj_1
	#解压到原始目录
	os.system(zlzlzlzl)
	print("已解压完成")
	print("\n如卡在此步可以按下回车")


def myyz():
	#用于验证密钥是否存在的函数
	with open(user_json_lj) as zx:
		number = json.load(zx)
	return number


def jcgx_zt():
	if jc_update():
		print("已检查到更新！\n")
		if os.path.exists(up_exe_lj):
			print("请关闭此应用后\n")
			print("点击桌面上的‘更新v2ray’\n")
			input("按下回车后关闭此应用！")
			sys.exit(0)
		try:
			print("正在下载更新文件！\n")
			get_update()
			print("已完成下载！\n")
			print("请关闭此应用后\n")
			print("点击桌面上的‘更新v2ray’\n")
			input("按下回车后关闭此应用！")
		except:
			print("更新失败!")
			print("错误！x004\n")
			input("按下任意键退出程序！")
		sys.exit(0)

def jcuser_cz_zt():
	ccz = []
	mac = get_MAC()
	phsz = "no"
	try:
		#检测密钥文件是否存在
		ccz = myyz()
		zh_lsxs = ccz[0]
		try:
			#读取个人偏好
			phsz = user_preference()
		except:
			phsz = "no"

		if phsz == "yes":
			print("您的帐号：" + zh_lsxs)
			print("\n如果您想切换账号或取消保存账号密码\n")
			print("可以输入“off”切换，无需变动按回车跳过！\n")
			qh = input("请输入(off/回车跳过)：")
			if qh == "off":
				print("关闭保存账号密码！")
				put_phsz("no")
				print("\n此次修改会在下一次启动生效")
				print("\n正在重新启动!\n")
				server_socks_zt()
			input("\n按下回车自动登录")
	except:
		#普通登陆函数
		print("在本地并没有您的存档文件\n")
		print("如没有注册请先注册！\n")
		print("请选择以下操作:\n")
		print("1.登陆账号\n")
		print("2.注册账号\n")
		xz = input("请输入选项的编号：")
		if xz == "1":
			print("\n请输入您的帐号\n")
			name = input("账号：")
			print("\n请输入您的密码\n")
			password = input("密码：")
			print("")
			phsz = input("是否保存账号密码？(yes/no)：")
			try:
				#加密个人信息
				name_jm = aes_a(keytxt,name)
				password_jm = aes_a(keytxt,password)
				mac_jm = aes_a(keytxt,mac)
			except:
				print("错误！X002")
				input("按下任意键退出程序！")
				sys.exit(0)
			try:
				#保存个人信息
				ccz = [name_jm, password_jm, mac_jm]
				put_key(ccz)
				put_phsz(phsz)
			except:
				print("错误！X004")
				input("按下任意键退出程序！")
				sys.exit(0)
		if xz == "2":
			ccz = ["zhuceqaz1","zhuceqaz1","zhuceqaz1"]
	return ccz, phsz

def server_zc_zt():
	#用于注册账号的函数
	ccz, preference = jcuser_cz_zt()
	name_jm = ccz[0]
	if name_jm == "zhuceqaz1":
		#注册账号的服务器连接
		sock = socket.socket()
		HOST = '60.205.221.103'
		PORT = 2233
		sock.connect((HOST, PORT))
		#发送模式
		sock.sendall("zc".encode())
		server_myd = sock.recv(1024).decode()
		while True:
			#输入账号
			print("\n请输入您的帐号(请不要输入中文)\n")
			name = input("账号：")
			#发送账号名称
			sock.sendall(name.encode())
			server_s = sock.recv(1024).decode()
			if server_s == "true_username":
				print("\n此用户名可用！\n")
				break
			else:
				print("\n此用户名已被注册！\n")
				print("请重新输入！\n")
		sock.close()
		#普通密码部分
		print("\n请输入您的密码\n")
		password = input("密码：")
		print("")
		preference = input("是否保存账号密码？(yes/no)：")
		try:
			#加密个人信息
			name_jm = aes_a(keytxt,name)
			password_jm = aes_a(keytxt,password)
		except:
			print("错误！X002")
			input("按下任意键退出程序！")
			sys.exit(0)
		try:
			#保存个人信息
			ccz = [name_jm, password_jm, mac_jm]
			put_key(ccz)
			put_phsz(preference)
		except:
			print("错误！X004")
			input("按下任意键退出程序！")
			sys.exit(0)

	return ccz, preference

def key_socks_zt():
	print("您的账户没有激活 或 激活已到期")
	key = input("您的卡密：")
	try:			
		#开始创建socks
		sock = socket.socket()
		HOST = '60.205.221.103'
		PORT = 2233
		sock.connect((HOST, PORT))
		#发送模式
		sock.sendall("key".encode())
		server_myd = sock.recv(1024).decode()
		#发送卡密
		sock.sendall(key.encode())
		server_s = sock.recv(1024).decode()
		sock.close()

		if server_s == "1":
			print("卡密添加成功！")
			print("正在重新启动")
			server_socks_zt()
		if server_s == "2":
			print("此卡密输入错误或已被激活！")
			prinr("卡密添加失败！")
			print("请重新输入！")
			key_socks_zt()
	except:
		print("错误！")
		input("按下任意键退出程序！")
		sys.exit(0)


def server_socks_zt():
	server_lb = []
	#用于访问服务器的主要函数
	ccz, preference = server_zc_zt()
	name_jm = ccz[0]
	password_jm = ccz[1]
	mac_jm = ccz[2]
	#开始创建socks
	sock = socket.socket()
	HOST = '60.205.221.103'
	PORT = 2233
	sock.connect((HOST, PORT))
	#发送模式
	sock.sendall("dl".encode())
	server_myd = sock.recv(1024).decode()
	#发送用户名
	sock.sendall(name_jm.encode())
	server_myd = sock.recv(1024).decode()
	#发送密码
	sock.sendall(password_jm.encode())
	server_myd = sock.recv(1024).decode()
	#发送mac号
	sock.sendall(mac_jm.encode())
	#接受服务器的状态码
	server_s = sock.recv(1024).decode()
	sock.close()
	#服务器命令分割
	server_lb = server_s.split('.')
	server_re = server_lb[0]
	server_time = server_lb[1]

	if server_re == "1":
		print("验证成功！\n")
		print("到期时间：" + server_time)
		print("")
		try:
			#下载配置文件
			getv2json()
		except:
			#下载错误反馈
			print("错误！X001\n")
			input("按下任意键退出程序！")
			sys.exit(0)
		try:
			#申请一个子进程开启删除配置文件脚本
			p = multiprocessing.Process(target=rmv2json)
			#运行脚本
			p.start()
			#主进程同时打开V2RAY
			mods.start_V2ray()
		except:
			#开启错误反馈
			print("错误！X003\n")
			input("按下任意键退出程序！")
			sys.exit(0)

	if server_re == "2":
		print("此账户不存在！\n")
		print("按下任意键重启程序！")
		input("重新输入账号密码")
		server_socks_zt()

	if server_re == "3":
		print("账户或密码输入错误！")
		print("按下任意键重启程序！")
		input("重新输入账号密码")
		server_socks_zt()

	if server_re == "4":
		print("您没有使用卡密激活或卡密激活时间已到")
		print("请输入新的卡密激活！")
		key_socks_zt()

	print("??????????????")
	print("您对服务器之间的通讯进行的干涉")
	input("按下任意键退出程序！")
	sys.exit(0)


def old_rm():
	#检测第二代程序
	one_old_az_lj = os.path.join(gzlj, "pythonz")
	if os.path.exists(one_old_az_lj):
		print("检测到旧版本的v2ray\n")
		print("第二代v2ray启动器！")
		print("正在卸载v2ray\n")
		try:
			remove_dir(one_old_az_lj)
		except:
			print("删除失败！")
			#删除错误反馈
			print("错误！X002\n")
			input("按下任意键退出程序！")
			sys.exit(0)
		print("删除完成!\n")


def installer():
	try:
		print("检测到此电脑并未安装最新的V2ray\n")
		#创建路径
		addlj()
	except:
		#创建路径错误反馈
		print("错误！X005\n")
		input("按下任意键退出程序！")
		sys.exit(0)
	try:
		#下载V2ray安装包并解压
		get_v2ray()
	except:
		#下载错误反馈
		print("错误！X006\n")
		input("按下任意键退出程序！")
		sys.exit(0)

	print("安装成功！\n")
	print("正在重新启动程序！\n")
	go()
