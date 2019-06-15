# -- coding:utf-8--
import os
import zipfile
from urllib import request
import time


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



def Schedule(a,b,c):
	#显示进度的函数
	per = 100.0 * a * b / c
	if per > 100 :
		per = 100
	print('%.2f%%' %(per))


def test_v2_ins(lj,yzlist):
	#用于验证v2ray是否安装完整的函数
	aaa = []

	test_re = True
	#用于测试程序是否安装的函数

	file_dir = lj
	for x_b, x_c, files in os.walk(file_dir):
		for x in files:
			aaa.append(x)

	bbb = yzlist

	for x in bbb:
		if x in aaa:
			test_re = True
		else:
			test_re = False
			break

	return test_re



def mkdir_v2lj(lj1,lj2):
	#创建v2ray安装下载路径的函数
	mblj_1 = lj1
	mblj_2 = lj2
	#创建路径的函数
	os.makedirs(mblj_1)
	os.makedirs(mblj_2)


def get_v2ray(sys,url,ziplj,jylj):

	if sys == "windows":

		#用于下载及安装v2ray的函数
		#v2ray服务器压缩包
		v2ray_server_rar_lj = url
		#v2ray本地压缩包
		v2ray_rar_lj = ziplj
		v2ray_rar_jy_lj = jylj
		print("正在下载V2ray资源包\n")
		print("这需要几分钟时间\n")
		#下载压缩包
		request.urlretrieve(v2ray_server_rar_lj, v2ray_rar_lj, Schedule)
		print("已下载完成压缩包")
		azip = zipfile.ZipFile(v2ray_rar_lj)
		#解压到原始目录
		azip.extractall(v2ray_rar_jy_lj)
		print("已解压完成")
		input("按下回车继续！")

	if sys == "macos":

		#v2ray服务器压缩包
		v2ray_server_rar_lj = url
		#v2ray本地压缩包
		v2ray_rar_lj = ziplj
		#权限修改
		jyhlj = jylj
		qx = "chmod 777 " + jyhlj + "/v2ray"
		qx2 = "chmod 777 " + jyhlj + "/v2ctl"

		print("正在下载V2ray资源包\n")
		print("这需要几分钟时间\n")
		#下载压缩包
		request.urlretrieve(v2ray_server_rar_lj, v2ray_rar_lj, Schedule)
		print("已下载完成压缩包")
		time.sleep(1)
		zlzlzlzl = "unzip -n " + v2ray_rar_lj + " -d " + jyhlj
		#解压到原始目录
		os.system(zlzlzlzl)
		os.system(qx)
		os.system(qx2)
		print("已解压完成")
		input("按下回车继续！")


def write_config(ip,uid,port,lj):

	with open(lj,encoding='UTF-8') as zx:
		pzz = json.load(zx)

	pzz["vmess"][0]["address"] = ip
	pzz["vmess"][0]["port"] = port
	pzz["vmess"][0]["id"] = uid


	with open(lj,'w') as ojbk:
		json.dump(pzz,ojbk)
	


def start_V2ray(ip,uid,port,Nlj,v2lj):

	write_config(ip,uid,port,Nlj)
	time.sleep(2)

	#os.popen(v2lj)

