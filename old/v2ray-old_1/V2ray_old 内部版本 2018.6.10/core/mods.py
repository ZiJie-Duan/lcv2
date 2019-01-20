# -- coding:utf-8--
from multiprocessing import Process
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json 

def get_keylb():
	url = "http://lucyx.cn/zzz/config.json"
	request.urlretrieve(url, r"C:\pythonX\unsers\key.txt")



def addlj():
	mblj_1 = r'C:\pythonX\sun36x64'
	mblj_2 = r'C:\pythonX\unsers'
	os.makedirs(mblj_1)
	os.makedirs(mblj_2)

def start_V2ray():
	os.system(r'C:\pythonX\sun36x64\v2ray-v3.25-windows-64\v2ray.exe')

def getv2json():
	url = "http://lucyx.cn/zzz/config.json"
	request.urlretrieve(url, r"C:\pythonX\sun36x64\v2ray-v3.25-windows-64\config.json")

def rmv2json():
	#延迟启动进行删除
	time.sleep(1)
	os.system(r'C:\pythonX\unsers\rmv2json.bat')

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

def put_time(a):
	#用于输出时间文件的函数
	#调用生成时间函数
	Xwltime = wl_time(a)
	#创建时间验证文件目录
	timejson = r'C:\pythonX\unsers\time.json'
	#写入json 时间
	with open(timejson,'w') as ls:
		json.dump(Xwltime,ls)

def get_v2ray():
	print("正在下载V2ray资源包\n")
	print("这需要几分钟时间\n")
	#声明url
	url = "http://60.205.221.103/v2ray/v2ray.zip"
	url_1 = "http://lucyx.cn/zzz/rmv2json.bat"
	#下载压缩包
	request.urlretrieve(url, r"C:\pythonX\sun36x64\a.zip")
	request.urlretrieve(url_1, r"C:\pythonX\unsers\rmv2json.bat")
	#读取压缩包
	azip = zipfile.ZipFile(r"C:\pythonX\sun36x64\a.zip")
	#解压到原始目录
	azip.extractall(r"C:\pythonX\sun36x64")


def timeyz():
	#用于验证时间是否可用的函数
	timejson = r'C:\pythonX\unsers\time.json'
	yzjg = False
	timex = now_time()
	with open(timejson) as zx:
		time = json.load(zx)
		print("到期时间：" + time)
		if time > timex:
			yzjg = True
		else:
			yzjg = False
	return yzjg



def jmyz(my):
	mwsz = my

	x = "lucycore"
	y = 0
	ctrlwith = 1

	xx = list(x)
	timea = time.strftime("%Y%m%d%H")
	timeb = str(timea)
	times = list(timeb)
	szmwlb = []
	XXX = int(times[-1]) * int(times[-2])

	while ctrlwith == 1:
		if y > 30:
			y = 0
			break
		y = y + 1
		yy = int(y) ** int(y) + XXX +int(timea)
		for zc in xx:
			if zc == "q":
				ys_1 = yy * 2
				szmwlb.append(ys_1)	
			if zc == "Q":
				ys_1 = yy ** 3
				szmwlb.append(ys_1)
			
			if zc == "w":
				ys_1 = yy * 4
				szmwlb.append(ys_1)
			if zc == "W":
				ys_1 = yy ** 5 
				szmwlb.append(ys_1)
			
			if zc == "r":
				ys_1 = yy * 6
				szmwlb.append(ys_1)
			if zc == "R":
				ys_1 = yy ** 7
				szmwlb.append(ys_1)
			
			if zc == "t":
				ys_1 = yy * 8
				szmwlb.append(ys_1)
			if zc == "T":
				ys_1 = yy ** 9
				szmwlb.append(ys_1)
			
			if zc == "y":
				ys_1 = yy * 10
				szmwlb.append(ys_1)
			if zc == "Y":
				ys_1 = yy ** 2
				szmwlb.append(ys_1)
			
			if zc == "u":
				ys_1 = yy * 11
				szmwlb.append(ys_1)
			if zc == "U":
				ys_1 = yy ** 3
				szmwlb.append(ys_1)
			
			if zc == "i":
				ys_1 = yy * 12
				szmwlb.append(ys_1)
			if zc == "I":
				ys_1 = yy ** 4
				szmwlb.append(ys_1)
			
			if zc == "o":
				ys_1 = yy * 13
				szmwlb.append(ys_1)
			if zc == "O":
				ys_1 = yy ** 5
				szmwlb.append(ys_1)
			
			if zc == "p":
				ys_1 = yy * 14
				szmwlb.append(ys_1)
			if zc == "P":
				ys_1 = yy ** 6
				szmwlb.append(ys_1)
			
			if zc == "e":
				ys_1 = yy * 15
				szmwlb.append(ys_1)
			if zc == "E":
				ys_1 = yy ** 7
				szmwlb.append(ys_1)
			
			
			
			if zc == "a":
				ys_1 = yy * 16
				szmwlb.append(ys_1)
			if zc == "A":
				ys_1 = yy ** 8
				szmwlb.append(ys_1)
			
			if zc == "s":
				ys_1 = yy * 17
				szmwlb.append(ys_1)
			if zc == "S":
				ys_1 = yy ** 9
				szmwlb.append(ys_1)
			
			if zc == "d":
				ys_1 = yy * 18
				szmwlb.append(ys_1)
			if zc == "D":
				ys_1 = yy ** 2
				szmwlb.append(ys_1)
			
			if zc == "f":
				ys_1 = yy * 19
				szmwlb.append(ys_1)
			if zc == "F":
				ys_1 = yy ** 3
				szmwlb.append(ys_1)
			
			if zc == "g":
				ys_1 = yy * 20
				szmwlb.append(ys_1)
			if zc == "G":
				ys_1 = yy ** 4
				szmwlb.append(ys_1)
			
			if zc == "h":
				ys_1 = yy * 21
				szmwlb.append(ys_1)
			if zc == "H":
				ys_1 = yy ** 5
				szmwlb.append(ys_1)
			
			if zc == "j":
				ys_1 = yy * 22
				szmwlb.append(ys_1)
			if zc == "J":
				ys_1 = yy ** 6
				szmwlb.append(ys_1)
			
			if zc == "k":
				ys_1 = yy * 23
				szmwlb.append(ys_1)
			if zc == "K":
				ys_1 = yy ** 7
				szmwlb.append(ys_1)
			
			if zc == "l":
				ys_1 = yy * 24
				szmwlb.append(ys_1)
			if zc == "L":
				ys_1 = yy ** 8
				szmwlb.append(ys_1)
			
			
			
			
			if zc == "z":
				ys_1 = yy * 25
				szmwlb.append(ys_1)
			if zc == "Z":
				ys_1 = yy ** 9
				szmwlb.append(ys_1)
			
			if zc == "x":
				ys_1 = yy * 26
				szmwlb.append(ys_1)
			if zc == "X":
				ys_1 = yy ** 2
				szmwlb.append(ys_1)
			
			if zc == "c":
				ys_1 = yy * 27
				szmwlb.append(ys_1)
			if zc == "C":
				ys_1 = yy ** 3
				szmwlb.append(ys_1)
				
			if zc == "v":
				ys_1 = yy * 28
				szmwlb.append(ys_1)
			if zc == "V":
				ys_1 = yy ** 4
				szmwlb.append(ys_1)
			
			if zc == "b":
				ys_1 = yy * 29
				szmwlb.append(ys_1)
			if zc == "B":
				ys_1 = yy ** 5
				szmwlb.append(ys_1)
			
			if zc == "n":
				ys_1 = yy * 30
				szmwlb.append(ys_1)
			if zc == "N":
				ys_1 = yy ** 6
				szmwlb.append(ys_1)
			
			if zc == "m":
				ys_1 = yy * 31
				szmwlb.append(ys_1)
			if zc == "M":
				ys_1 = yy ** 7
				szmwlb.append(ys_1)
				
		mwzh_3 = []
		for mwzh in szmwlb:
			mwzh_1 = str(mwzh)
			mwzh_3.append(mwzh_1)
			
		mw = ''.join(mwzh_3)
		
		szmwlb = []
		
		if mw == mwsz:
			ctrlwith = 2
	return y
