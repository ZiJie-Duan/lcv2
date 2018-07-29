# -- coding:utf-8--
import json

#---------------------------------------------------------------------------------------
#卡密生成模块
key_zd = {}

def mod_1():	
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
	hhz = 0
	with open("key.txt") as xxx:
		for key_zlq in xxx:
			hhz = hhz + 1
			keyzl_1 = str(hhz) + " " + key_zlq
			with open("key_1.txt",'a') as hii:
				hii.write(keyzl_1)


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

def kmsc_bt():
	print("请选择生成模式\n")
	print("1.手动输入生成 2.大批量导入生成 3.爱发卡整理\n")
	mod = input("请选择数字：\n")
	if mod > "0" and mod < "4":
		modxzhs(mod)

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

def help():
	#api列表
	print("")
	print("--------------userk操作---------------")
	print("")
	print("ukl--------列出userk所有用户信息")
	print("uklb-------列出userk所有标记用户的信息")
	print("ukcz-------使用密钥查找userk用户")
	print("ukczn------使用名称查找userk用户")
	print("ukrot------使用mac修改userk用户等级")
	print("ukx--------使用mac写入userk用户操作命令")
	print("")
	print("--------------卡密操作---------------")
	print("")
	print("kmsc-------启动卡密生成模块")
	print("")

#---------------------------------------------------------------------------------------

def core():
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

	if core_ml == "kmsc":
		try:
			kmsc_bt()
		except:
			print("错误！函数kmsc_bt")

	if core_ml == "uklb":
		try:
			dq_userk_lcbj()
		except:
			print("错误！函数dq_userk_lcbj")

	if core_ml == "ukcz":
		try:
			dq_userk_cz_key()
		except:
			print("错误！函数dq_userk_cz_key")

	if core_ml == "ukczn":
		try:
			dq_userk_cz_name()
		except:
			print("错误！函数dq_userk_cz_name")

	if core_ml == "ukrot":
		try:
			xr_userk_rot()
		except:
			print("错误！函数xr_userk_rot")

	if core_ml == "ukx":
		try:
			xr_userk_xml()
		except:
			print("错误！函数xr_userk_xml")


	if core_ml == "q!":
		sys.exit(0)

	core()

print("\nlucycore v2ray工具箱\n")
core()
