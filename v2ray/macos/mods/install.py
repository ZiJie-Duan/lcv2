# -- coding:utf-8--
import os
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

def del_v2():
	gzlj = os.getcwd()
	lj = os.path.join(gzlj, "pythonz5.1")
	remove_dir(lj)



def Schedule(a,b,c):
    #显示进度的函数
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' %(per))


def t_v2():
    gzlj = os.getcwd()
    lj = os.path.join(gzlj, "pythonz5.1")
    aaa = []
    test_re = True
    #用于测试程序是否安装的函数

    file_dir = lj
    for x_b, _c, files in os.walk(file_dir):
        for x in files:
            aaa.append(x)
    bbb = ['V.zip', 'geoip.dat', 'geosite.dat', 'v2ctl', 'v2ray', 'v2ray.sig']
    for x in bbb:
        if x in aaa:
            test_re = True
        else:
            test_re = False
            break
    return test_re



def addlj():
	gzlj = os.getcwd()
	mblj_1 = os.path.join(gzlj, "pythonz5.1", "sun36x64")
	mblj_2 = os.path.join(gzlj, "pythonz5.1", "unsers")
	#创建路径的函数
	os.makedirs(mblj_1)
	os.makedirs(mblj_2)



def get_v2ray():

    #v2ray服务器压缩包
    v2ray_server_rar_lj = "http://www.lucycore.top/v2ray/v2rayMac.zip"

    gzlj = os.getcwd()
    v2ray_rar_lj = os.path.join(gzlj, "pythonz5.1", "sun36x64", "V.zip")
    v2ray_rar_jy_lj = os.path.join(gzlj, "pythonz5.1", "sun36x64")

    #权限修改
    jyhlj = os.path.join(gzlj, "pythonz5.1", "sun36x64")
    qx = "chmod 777 " + jyhlj + "/v2ray"
    qx2 = "chmod 777 " + jyhlj + "/v2ctl"

    print("正在下载V2ray资源包\n")
    print("这需要几分钟时间\n")
    #下载压缩包
    request.urlretrieve(v2ray_server_rar_lj, v2ray_rar_lj, Schedule)
    print("已下载完成压缩包")
    time.sleep(1)
    zlzlzlzl = "unzip -n " + v2ray_rar_lj + " -d " + v2ray_rar_jy_lj
    #解压到原始目录
    os.system(zlzlzlzl)
    os.system(qx)
    os.system(qx2)
    print("已解压完成")
    input("按下回车继续！")

