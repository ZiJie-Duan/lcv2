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

keytxt = "LucycoreX"

#工作路径
gzlj = os.getcwd()
#是否有更新验证文件位置
update_json_url = "http://lucyx.cn/zzz/v2ray/update.json"
#服务器更新文件位置
update_exe_url = "http://60.205.221.103/v2ray/v2rayWinX.zip"
#更新验证文件位置
up_json_lj = r"C:\pythonz4\unsers\update.json"
#更新插件位置
up_exe_lj = os.path.join(gzlj, "v2rayWinX.zip")

#创建的根目录
mblj_1 = r'C:\pythonz4\sun36x64'
mblj_2 = r'C:\pythonz4\unsers'

#动态命令对照文件服务器位置
dtml_dz_ml = "http://lucyx.cn/zzz/v2ray/dtml.json"
#动态命令对照文件本地位置
dtml_dz_ml_bd = "C:/pythonz4/unsers/dtml.json"
#动态命令正文本地位置
dtml_dz_ml_bd_zw = "C:/pythonz4/unsers/dtmlzw.txt"


#v2ray本体路径
v2ray_start_lj = r'C:\pythonz4\sun36x64\v2ray\v2ray.exe'
#v2ray json文件服务器位置
v2ray_server_json_lj = "http://lucyx.cn/zzz/v2ray/v2_config_1.json"
#v2ray 本地json文件位置
v2ray_json_lj = r"C:\pythonz4\sun36x64\v2ray\config.json"

#key json本地位置
key_json_lj = r'C:\pythonz4\unsers\key.json'

#v2ray服务器压缩包
v2ray_server_rar_lj = "http://60.205.221.103/v2ray/v2rayWin.zip"

#v2ray本地压缩包
v2ray_rar_lj = r"C:\pythonz4\sun36x64\V.zip"
v2ray_rar_jy_lj = r"C:\pythonz4\sun36x64"

#用户偏好设置文件
user_phsz_json_lj = r"C:\pythonz4\unsers\Preference.json"

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
	if edition == 5 :
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

def rmv2key():
	#删除key文件
	os.remove(key_json_lj)

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
	azip = zipfile.ZipFile(v2ray_rar_lj)
	#解压到原始目录
	azip.extractall(v2ray_rar_jy_lj)
	print("已解压完成")
	print("\n如卡在此步可以按下回车")


def myyz():
	#用于验证密钥是否存在的函数
	with open(key_json_lj) as zx:
		number = json.load(zx)
	return number


def jcgx_zt():
	if jc_update():
		print("已检查到更新！\n")
		if os.path.exists(up_exe_lj):
			print("请关闭此应用后\n")
			print("解压并打开根目录的‘v2rayWinX.zip’\n")
			input("按下回车后关闭此应用！")
			sys.exit(0)
		try:
			print("正在下载更新文件！\n")
			get_update()
			print("已完成下载！\n")
			print("请关闭此应用后\n")
			print("点击根目录的‘更新v2ray’\n")
			input("按下回车后关闭此应用！")
		except:
			print("更新失败!")
			print("错误！x004\n")
			input("按下任意键退出程序！")
		sys.exit(0)


def old_rm():

	#检测第一代程序
	one_old_az_lj = os.path.join(r"C:\pythonX")
	if os.path.exists(one_old_az_lj):
		print("检测到旧版本的v2ray\n")
		print("第一代v2ray启动器！")
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

	#检测第二代程序
	one_old_az_lj = os.path.join(r"C:\pythonz")
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


def install():
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


def get_dtml_dzb():
	#用于获取特殊命令对照目录的函数
	request.urlretrieve(dtml_dz_ml, dtml_dz_ml_bd)

def get_dtml_xsdz(wz):
	#用于获取特殊命令对照目录的函数
	request.urlretrieve(wz, dtml_dz_ml_bd_zw)


def dq_dtml_ml(x):
	#用于读取动态命令目录的函数
	with open(dtml_dz_ml_bd) as zx:
		dtml_ml = json.load(zx)
	ml_dz = dtml_ml[x]
	return ml_dz


def dtml_srjc(Xx):
	#用于判断并执行特殊命令的函数
	if Xx == "0":
		print("")
	else:
		#获取命令对照表
		get_dtml_dzb()
		wz = dq_dtml_ml(Xx)
		#下载命令正文
		get_dtml_xsdz(wz)
		#读取并运行命令
		with open(dtml_dz_ml_bd_zw) as xxx:
			for hii in xxx: 
				exec(hii)

def core():
#.......................................................................
	cfz = 0
	try:
		data = myyz()
	except:
		cfz = 1
		print("您还没有激活！\n")
		key = input("请输入密钥：")
		data = key
		try:
			#尝试写入密钥json
			put_key(key)
		except:
			print("写入失败！")
			print("错误！X007\n")
			input("按下任意键退出程序！")
			sys.exit(0)
		try:
			#获取mac号
			mac = get_MAC()
			#开始创建socks
			sock = socket.socket()
			HOST = '60.205.221.103'
			PORT = 2233
			sock.connect((HOST, PORT))
			#发送模式
			sock.sendall("key".encode())
			server_myd = sock.recv(1024).decode()
			#发送key
			sock.sendall(data.encode())
			server_myd = sock.recv(1024).decode()
			#发送mac号
			sock.sendall(mac.encode())
			#接受服务器的状态码
			server_s = sock.recv(1024).decode()
			sock.close()
			#服务器命令分割
			server_lb = server_s.split('.')
			server_re = server_lb[0]
			server_time = server_lb[1]
			server_ml = server_lb[2]
		except:
			print("连接失败！")
			print("错误！X008\n")
			input("按下任意键退出程序！")
			sys.exit(0)

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
				start_V2ray()
			except:
				#开启错误反馈
				print("错误！X003\n")
				input("按下任意键退出程序！")
				sys.exit(0)

		if server_re == "2":
			print("此密钥不存在！\n")
			print("按下任意键重启程序！")
			input("重新输入密钥")
			rmv2key()
			core()

		print("??????????????")
		print("您对服务器之间的通讯进行的干涉")
		input("按下任意键退出程序！")
		sys.exit(0)

	#.............................................................
	
	if cfz == 0:
		try:
			#获取mac号
			mac = get_MAC()
			#开始创建socks
			sock = socket.socket()
			HOST = '60.205.221.103'
			PORT = 2233
			sock.connect((HOST, PORT))
			#发送模式
			sock.sendall("mac".encode())
			server_myd = sock.recv(1024).decode()
			#发送key
			sock.sendall(data.encode())
			server_myd = sock.recv(1024).decode()
			#发送mac号
			sock.sendall(mac.encode())
			#接受服务器的状态码
			server_s = sock.recv(1024).decode()
			sock.close()
			#服务器命令分割
			server_lb = server_s.split('.')
			server_re = server_lb[0]
			server_time = server_lb[1]
			server_ml = server_lb[2]
			server_x = server_lb[3]
		except:
			print("连接失败！")
			print("错误！X008\n")
			input("按下任意键退出程序！")
			sys.exit(0)

		try:
			#特殊指令函数
			dtml_srjc(server_x)
		except:
			print("E")
			print("")

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
				start_V2ray()
			except:
				#开启错误反馈
				print("错误！X003\n")
				input("按下任意键退出程序！")
				sys.exit(0)

		if server_re == "2":
			print("此密钥不存在！\n")
			print("按下任意键重启程序！")
			input("重新输入密钥")
			rmv2key()
			core()

		if server_re == "3":
			print("此密钥已过期！")
			print("按下任意键重启程序！")
			input("重新输入密钥")
			rmv2key()
			core()

		if server_re == "4":
			print("\nLucy core 超级用户\n")
			print("验证成功！")
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
				start_V2ray()
			except:
				#开启错误反馈
				print("错误！X003\n")
				input("按下任意键退出程序！")
				sys.exit(0)


		print("??????????????")
		print("您对服务器之间的通讯进行的干涉")
		input("按下任意键退出程序！")
		sys.exit(0)

