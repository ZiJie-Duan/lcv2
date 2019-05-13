# -- coding:utf-8--
import os


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


def old_rm(syss):

if syss == "windows":

	oldlj = [r"C:\pythonX",r"C:\pythonz",r"C:\pythonz4",r"C:\pythonz5"] 

	for x in oldlj:

		if os.path.exists(x):
			print("检测到旧版本的v2ray\n")
			print("正在卸载v2ray\n")
			try:
				remove_dir(x)
			except:
				print("删除失败！")
				#删除错误反馈
				print("程序错误！移除旧版本错误！\n")
				input("按下任意键退出程序！")
				sys.exit(0)
			print("删除完成!\n")

