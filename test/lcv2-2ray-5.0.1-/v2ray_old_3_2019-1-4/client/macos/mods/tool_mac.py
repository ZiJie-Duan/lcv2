# -- coding:utf-8--
import json
import paramiko
import re
import os
from urllib import request


#---------------------------------------------------------------------------------------

def start_v2():
	gzlj = os.getcwd()
	key_json_lj = os.path.join(gzlj, "pythonz5", "sun36x64", "v2ray", "config.json")
	request.urlretrieve(r"http://60.205.221.103/zzz/v2ray/v2_config_1.json", key_json_lj)
	v2ray_start_lj = os.path.join(gzlj, "pythonz5", "sun36x64", "v2ray", "v2ray")
	os.system(v2ray_start_lj)

#---------------------------------------------------------------------------------------

def get_v2_json():
	#获取v2ray的配置文件
	gzlj = os.getcwd()
	v2ray_server_json_lj = "http://60.205.221.103/zzz/v2ray/v2_config_1.json"
	lj = os.path.join(gzlj, "Desktop", "config.json")
	request.urlretrieve(v2ray_server_json_lj, lj)

#---------------------------------------------------------------------------------------

def v2ray_lj_rm():
#用于删除v2ray安装的函数
	gzlj = os.getcwd()
	old_python_4 = os.path.join(gzlj, "pythonz5")
	remove_dir(old_python_4)

#---------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------

def v2ray_key_rm():
#用于删除用户key的函数
	gzlj = os.getcwd()
	key_json_lj = os.path.join(gzlj, "pythonz5", "unsers", "key.json")
	os.remove(key_json_lj)

#---------------------------------------------------------------------------------------

def root_tool():
	#用于启动工具的函数
	gzlj = os.getcwd()
	root_lj = os.path.join(gzlj, "Desktop", "lucycore.txt")
	try:
		with open(root_lj) as xxx:
			beee = xxx.read()

		if beee == "v2ray.tool":
			tool_core()

	except:
		a = 2


#---------------------------------------------------------------------------------------

def remove_rz():
	#删除rz.txt的函数
	ps = input("server_password：")
	client = paramiko.SSHClient()

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect('60.205.221.103', username='root', password=ps, timeout=5)

	client.exec_command('rm /zzz/rz.txt')

#---------------------------------------------------------------------------------------

def get_rz_txt():
	#下载日志文件模块
	#用于获取rz.txt的函数
	ps = input("server_password：")
	transport = paramiko.Transport(('60.205.221.103', 22))
	transport.connect(username='root', password=ps)
	
	sftp = paramiko.SFTPClient.from_transport(transport)
	
	sftp.get('/zzz/rz.txt', 'rz.txt')
	
	transport.close()



#---------------------------------------------------------------------------------------
#卡密生成模块

def mod_1():
	key_zd = {}
	while True :
		key = input("密钥名称：")
		key_z = input("密钥时间：")
		if key_z == "0":
			print("退出写入\n")
			input()
			break
		key_zd[key] = int(key_z)


	with open("key.json",'w') as ojbk_1:
		json.dump(key_zd,ojbk_1)


def mod_2():
	key_zd = {}
	while True :
		key_z = input("请输入此批密钥时间")
		if key_z == "0":
			print("退出写入\n")
			input()
			break
		with open("key.txt") as xxx:
			for key_zlq in xxx:
				print("写入：" + key_zlq)
				key_zlqa = key_zlq[:-1]
				key_zd[key_zlqa] = int(key_z)

	with open("key.json",'w') as ojbk_1:
		json.dump(key_zd,ojbk_1)

def mod_3():
	key_zd = {}
	hhz = 0
	with open("key.txt") as xxx:
		for key_zlq in xxx:
			hhz = hhz + 1
			keyzl_1 = str(hhz) + " " + key_zlq
			with open("key_1.txt",'a') as hii:
				hii.write(keyzl_1)

def mod_4():
	key_zd = {}

	zl = input("数量(2-5)：")

	if zl == "2":

		with open("1.json") as zx:
			zd_1 = json.load(zx)

		with open("2.json") as zx:
			zd_2 = json.load(zx)

		zd_3 = {}
		zd_3.update(zd_1)
		zd_3.update(zd_2)

		with open("key.json",'w') as ojbk:
			json.dump(zd_3,ojbk)

	if zl == "3":

		with open("1.json") as zx:
			zd_1 = json.load(zx)

		with open("2.json") as zx:
			zd_2 = json.load(zx)

		with open("3.json") as zx:
			zd_4 = json.load(zx)

		zd_3 = {}
		zd_3.update(zd_1)
		zd_3.update(zd_2)
		zd_3.update(zd_4)

		with open("key.json",'w') as ojbk:
			json.dump(zd_3,ojbk)

	if zl == "4":

		with open("1.json") as zx:
			zd_1 = json.load(zx)

		with open("2.json") as zx:
			zd_2 = json.load(zx)

		with open("3.json") as zx:
			zd_4 = json.load(zx)

		with open("4.json") as zx:
			zd_5 = json.load(zx)

		zd_3 = {}
		zd_3.update(zd_1)
		zd_3.update(zd_2)
		zd_3.update(zd_4)
		zd_3.update(zd_5)

		with open("key.json",'w') as ojbk:
			json.dump(zd_3,ojbk)

	if zl == "5":

		with open("1.json") as zx:
			zd_1 = json.load(zx)

		with open("2.json") as zx:
			zd_2 = json.load(zx)

		with open("3.json") as zx:
			zd_4 = json.load(zx)

		with open("4.json") as zx:
			zd_5 = json.load(zx)

		with open("5.json") as zx:
			zd_6 = json.load(zx)

		zd_3 = {}
		zd_3.update(zd_1)
		zd_3.update(zd_2)
		zd_3.update(zd_4)
		zd_3.update(zd_5)
		zd_3.update(zd_6)

		with open("key.json",'w') as ojbk:
			json.dump(zd_3,ojbk)


def modxzhs(mod):
	
	if mod == "1":
		print("开始运行mod1\n")
		mod_1()

	if mod == "2":
		print("开始运行mod2\n")
		mod_2()

	if mod == "3":
		print("开始运行mod3\n")
		mod_3()

	if mod == "4":
		print("开始运行mod4\n")
		mod_4()

def kmsc_bt():
	print("请选择生成模式\n")
	print("1.手动输入生成 2.大批量导入生成 3.爱发卡整理")
	print("4.二次添加卡密\n")
	mod = input("请选择数字：")
	if mod > "0" and mod < "5":
		modxzhs(mod)

#---------------------------------------------------------------------------------------

def rz_fx():
	#分析日志内容
	gl = False
	a = input("是否过滤无标记用户？[y/n]：")

	if a == "y":
		gl = True
	if a == "n":
		gl = False

	#日志
	user_rz = "rz.txt"
	#逐行读取文件
	with open(user_rz, encoding='UTF-8') as xxx:
		for hii in xxx:
			time = re.match(r'.{4}(-..){5}', hii)
			if time:
				time_now = hii.strip("\n")

			mac = re.match(r'(..:){5}..', hii)
			if mac:
				userklj = "userk.json"
				hii = hii.strip("\n")
				#打开用户信息文件
				with open(userklj) as zx_1:
					userk = json.load(zx_1)
				#读取详细信息
				for key, value in userk.items():
					keyy = value[0]
					time = value[1]
					root = value[2]
					x = value[3]
					try:
						bjname = value[4]
					except:
						bjname = "no_name"
					if key == hii:
						if gl == True:
							if bjname != "no_name":
								print("\n\n" + time_now)
								print("名称：" + bjname)
								print("密钥：" + keyy)
								print("时间：" + time)
								if root == True:
									rootx = "True"
								else:
									rootx = "False"
								print("等级：" + rootx)
								print("指令：" + x)
						else:
							print("\n\n" + time_now)
							print("名称：" + bjname)
							print("密钥：" + keyy)
							print("时间：" + time)
							if root == True:
								rootx = "True"
							else:
								rootx = "False"
							print("等级：" + rootx)
							print("指令：" + x)
							
							

#---------------------------------------------------------------------------------------

#使用mac查询用户信息
def userk_c_mac():
	#用户信息库
	userklj = "userk.json"
	mac = input("mac：")
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)
	#读取详细信息
	for key, value in userk.items():
		keyy = value[0]
		time = value[1]
		root = value[2]
		x = value[3]
		try:
			bjname = value[4]
		except:
			bjname = "no_name"
		if key == mac:
			print("密钥：" + keyy)
			print("时间：" + time)
			if root == True:
				rootx = "True"
			else:
				rootx = "False"
			print("等级：" + rootx)
			print("指令：" + x)
			print("名称：" + bjname)


#---------------------------------------------------------------------------------------

#用于统一修改用户特殊指令的函数
def userk_x_pl():
	#用户信息库
	userklj = "userk.json"
	a = input("数值：")
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)
	#读取详细信息
	for key, value in userk.items():
		value[3] = a

	with open(userklj,'w') as ojbk_1:
		json.dump(userk,ojbk_1)



#---------------------------------------------------------------------------------------

def dq_userk():
	#用户信息库
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)
	#验证key是否存在
	for key, value in userk.items():
		keyy = value[0]
		time = value[1]
		root = value[2]
		x = value[3]
		try:
			name = value[4]
		except:
			name = "无"
		print("")
		print("用户名称：" + name)
		print("用户mac：" + key)
		print("密钥：" + keyy)
		print("时间：" + time)
		if root:
			print("root：True")
		else:
			print("root：False")
		print("命令标记：" + x)
		print("")

#---------------------------------------------------------------------------------------

def dq_userk_lcbj():
	#用于列出标记过后的用户
	#用户信息库
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)
	#验证key是否存在
	for key, value in userk.items():
		keyy = value[0]
		time = value[1]
		root = value[2]
		x = value[3]
		try:
			name = value[4]
			print("")
			print("用户名称：" + name)
			print("用户mac：" + key)
			print("密钥：" + keyy)
			print("时间：" + time)
			if root:
				print("root：True")
			else:
				print("root：False")
			print("命令标记：" + x)
			print("")
		except:
			name = "无"

#---------------------------------------------------------------------------------------

def dq_userk_cz_key():
	#用于使用密钥查找用户
	key_sr = input("密钥：")
	#用户信息库
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)
	#验证key是否存在
	for key, value in userk.items():
		keyy = value[0]
		time = value[1]
		root = value[2]
		x = value[3]
		try:
			name = value[4]
		except:
			name = "无"
		if key_sr == keyy:
			print("")
			print("用户名称：" + name)
			print("用户mac：" + key)
			print("密钥：" + keyy)
			print("时间：" + time)
			if root:
				print("root：True")
			else:
				print("root：False")
			print("命令标记：" + x)
			print("")


#---------------------------------------------------------------------------------------

def dq_userk_cz_name():
	#用于使用标记名称查找用户
	name_sr = input("名称：")
	#用户信息库
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)
	#验证key是否存在
	for key, value in userk.items():
		keyy = value[0]
		time = value[1]
		root = value[2]
		x = value[3]
		try:
			name = value[4]
		except:
			name = "无"
		if name_sr == name:
			print("")
			print("用户名称：" + name)
			print("用户mac：" + key)
			print("密钥：" + keyy)
			print("时间：" + time)
			if root:
				print("root：True")
			else:
				print("root：False")
			print("命令标记：" + x)
			print("")

#---------------------------------------------------------------------------------------

def xr_userk_rot():
	#用于修改用户权限的函数
	macc = input("mac号:")
	zbz = input("y/n:")
	#用户信息库
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)

	user_xx = userk[macc]
	if zbz == "y":
		user_xx[2] = True
		print("添加权限")
	if zbz == "n":
		user_xx[2] = False
		print("删除权限")

	userk[macc] = user_xx

	with open(userklj,'w') as ojbk_1:
		json.dump(userk,ojbk_1)


#---------------------------------------------------------------------------------------

def xr_userk_xml():
	#用于修改用户权限的函数
	print("删除命令标记输入“del”")
	macc = input("mac号:")
	zbz = input("命令:")
	#用户信息库
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)

	user_xx = userk[macc]
	if zbz == "del":
		user_xx[3] = "0"
		print("删除命令")
	else:
		user_xx[3] = zbz
		print("添加命令")

	userk[macc] = user_xx

	with open(userklj,'w') as ojbk_1:
		json.dump(userk,ojbk_1)

#---------------------------------------------------------------------------------------

def xr_userk_namebj():
	#用于修改用户名称标记的函数
	print("删除名称标记输入“del”")
	macc = input("mac号:")
	zbz = input("名称:")
	#用户信息库
	userklj = "userk.json"
	#打开用户信息文件
	with open(userklj) as zx_1:
		userk = json.load(zx_1)

	user_xx = userk[macc]
	if zbz == "del":
		del user_xx[4]
		print("删除名称")
	else:
		try:
			del user_xx[4]
			print("尝试覆盖历史名称")
		except:
			print("无历史名称")
		user_xx.insert(4, zbz)
		print("添加名称")

	userk[macc] = user_xx

	with open(userklj,'w') as ojbk_1:
		json.dump(userk,ojbk_1)

#---------------------------------------------------------------------------------------

def get_userk_json():
	#用于获取userk.json的函数
	ps = input("server_password：")
	transport = paramiko.Transport(('60.205.221.103', 22))
	transport.connect(username='root', password=ps)
	 
	sftp = paramiko.SFTPClient.from_transport(transport)
	 
	sftp.get('/zzz/userk.json', 'userk.json')
	 
	transport.close()

#---------------------------------------------------------------------------------------

def get_key_json():
	#用于获取key.json的函数
	ps = input("server_password：")
	transport = paramiko.Transport(('60.205.221.103', 22))
	transport.connect(username='root', password=ps)
	 
	sftp = paramiko.SFTPClient.from_transport(transport)
	 
	sftp.get('/zzz/key.json', 'key.json')
	 
	transport.close()

#---------------------------------------------------------------------------------------


def put_userk_json():
	#用于上传userk.json的函数
	ps = input("server_password：")
	transport = paramiko.Transport(('60.205.221.103', 22))
	transport.connect(username='root', password=ps)
	 
	sftp = paramiko.SFTPClient.from_transport(transport)
	 
	sftp.put('userk.json', '/zzz/userk.json')
	 
	transport.close()

#---------------------------------------------------------------------------------------

def put_key_json():
	#用于上传key.json的函数
	ps = input("server_password：")
	transport = paramiko.Transport(('60.205.221.103', 22))
	transport.connect(username='root', password=ps)
	 
	sftp = paramiko.SFTPClient.from_transport(transport)
	 
	sftp.put('key.json', '/zzz/key.json')
	 
	transport.close()

#---------------------------------------------------------------------------------------

def ssh_user_rm_key():
	#删除key.json的函数
	ps = input("server_password：")
	client = paramiko.SSHClient()

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect('60.205.221.103', username='root', password=ps, timeout=5)

	client.exec_command('rm /zzz/key.json')

#---------------------------------------------------------------------------------------

def ssh_user_rm_userk():
	#删除userk.json的函数
	ps = input("server_password：")
	client = paramiko.SSHClient()

	client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

	client.connect('60.205.221.103', username='root', password=ps, timeout=5)

	client.exec_command('rm /zzz/userk.json')

#---------------------------------------------------------------------------------------

def help():
	#api列表
	print("")
	print("--------------v2ray操作---------------")
	print("")
	print("rmv2k------删除v2ray本地的key.json")
	print("rmv2-------删除整个v2ray本地的安装痕迹")
	print("")
	print("gv2json----获取v2ray配置文件")
	print("sv2--------直接启动v2ray服务")
	print("")
	print("")
	print("--------------userk操作---------------")
	print("")
	print("ukl--------列出userk所有用户信息")
	print("uklb-------列出userk所有标记用户的信息")
	print("umac-------mac查询userk用户的信息")
	print("")
	print("mc---------使用密钥查找userk用户")
	print("nc---------使用名称查找userk用户")
	print("")
	print("ur---------使用mac修改userk用户等级")
	print("un---------使用mac写入userk用户名称标记")
	print("")
	print("ux---------使用mac写入userk用户操作命令")
	print("ng---------统一修改所有userk用户操作命令")
	print("")
	print("--------------卡密操作---------------")
	print("")
	print("km---------启动卡密生成模块")
	print("")
	print("-------------server操作--------------")
	print("")
	print("guk--------获取server中的userk.json")
	print("gky--------获取server中的key.json")
	print("")
	print("puk--------上传本地的userk.json")
	print("pky--------上传本地的key.json")
	print("")
	print("rmkey------删除server中的key.json")
	print("rmuserk----删除server中的userk.json")
	print("")
	print("------------日志文件操作-------------")
	print("")
	print("grz--------下载日志文件")
	print("rmrz-------删除服务器日志文件")
	print("rzfx-------分析日志文件")
	print("")

#---------------------------------------------------------------------------------------

def tool_core():
	#核心

	core_ml = input("core：")

	if core_ml == "help":
		try:
			help()
		except:
			print("错误！函数help")

	if core_ml == "ukl":
		try:
			dq_userk()
		except:
			print("错误！函数dq_userk")

	if core_ml == "km":
		try:
			kmsc_bt()
		except:
			print("错误！函数kmsc_bt")

	if core_ml == "uklb":
		try:
			dq_userk_lcbj()
		except:
			print("错误！函数dq_userk_lcbj")

	if core_ml == "mc":
		try:
			dq_userk_cz_key()
		except:
			print("错误！函数dq_userk_cz_key")

	if core_ml == "nc":
		try:
			dq_userk_cz_name()
		except:
			print("错误！函数dq_userk_cz_name")

	if core_ml == "ur":
		try:
			xr_userk_rot()
		except:
			print("错误！函数xr_userk_rot")

	if core_ml == "ux":
		try:
			xr_userk_xml()
		except:
			print("错误！函数xr_userk_xml")

	if core_ml == "un":
		try:
			xr_userk_namebj()
		except:
			print("错误！函数xr_userk_namebj")

	if core_ml == "guk":
		try:
			get_userk_json()
		except:
			print("错误！函数get_userk_json")

	if core_ml == "gky":
		try:
			get_key_json()
		except:
			print("错误！函数get_key_json")

	if core_ml == "rmkey":
		try:
			ssh_user_rm_key()
		except:
			print("错误！函数ssh_user_rm_key")

	if core_ml == "rmuserk":
		try:
			ssh_user_rm_userk()
		except:
			print("错误！函数ssh_user_rm_userk")

	if core_ml == "pky":
		try:
			put_key_json()
		except:
			print("错误！函数ssh_user_rm_userk")

	if core_ml == "puk":
		try:
			put_userk_json()
		except:
			print("错误！函数ssh_user_rm_userk")

	if core_ml == "ng":
		try:
			userk_x_pl()
		except:
			print("错误！函数userk_x_pl")

	if core_ml == "umac":
		try:
			userk_c_mac()
		except:
			print("错误！函数userk_c_mac")

	if core_ml == "rzfx":
		try:
			rz_fx()
		except:
			print("错误！函数rz_fx")

	if core_ml == "grz":
		try:
			get_rz_txt()
		except:
			print("错误！函数get_rz_txt")

	if core_ml == "rmrz":
		try:
			remove_rz()
		except:
			print("错误！函数get_rz_txt")

	if core_ml == "rmv2k":
		try:
			v2ray_key_rm()
		except:
			print("错误！函数v2ray_key_rm")

	if core_ml == "rmv2":
		try:
			v2ray_lj_rm()
		except:
			print("错误！函数v2ray_lj_rm")

	if core_ml == "gv2json":
		try:
			get_v2_json()
		except:
			print("错误！函数get_v2_json")

	if core_ml == "sv2":
		try:
			start_v2()
		except:
			print("错误！函数start_v2")


	if core_ml == "q!":
		sys.exit(0)
	tool_core()

