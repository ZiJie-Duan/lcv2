# -- coding:utf-8--
import json

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


def modxzhs():
	
	if mod == "1":
		print("开始运行mod1\n")
		mod_1()

	if mod == "2":
		print("开始运行mod2\n")
		mod_2()

	if mod == "3":
		print("开始运行mod3\n")
		mod_3()

def hhhhhh():

	if mod > "0" and mod < "4":
		modxzhs()
	else :
		print("数字输入错误！")
		print("请重新输入！")
		hhhhhh()

print("\n密钥生成器\n")

print("请选择生成模式\n")
print("1.手动输入生成 2.大批量导入生成 3.爱发卡整理\n")
mod = input("请选择数字：\n")


hhhhhh()