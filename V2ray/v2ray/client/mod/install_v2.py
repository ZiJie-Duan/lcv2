# -- coding:utf-8--
import os
import zipfile
from urllib import request


def Schedule(a,b,c):
    #显示进度的函数
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' %(per))


def t_v2(sys):
    aaa = []
    test_re = True
    #用于测试程序是否安装的函数
    if sys == "windows":
        file_dir = r"C:\pythonz5"
        for x_b, _c, files in os.walk(file_dir):
            for x in files:
                aaa.append(x)
        bbb = ['V.zip', 'geoip.dat', 'geosite.dat', 'readme.md', 'v2ctl.exe', 'v2ctl.exe.sig', 'v2ray.exe', 'v2ray.exe.sig', 'wv2ray.exe', 'wv2ray.exe.sig']
        for x in bbb:
            if x in aaa:
                test_re = True
            else:
                test_re = False
                break
        return test_re
    else:
        #工作路径
        gzlj = os.getcwd()
        file_dir = os.path.join(gzlj, "pythonz5")
        for x_b, _c, files in os.walk(file_dir):
            for x in files:
                aaa.append(x)
        bbb = ['V.zip', 'geoip.dat', 'geosite.dat', 'readme.md', 'v2ctl.exe', 'v2ctl.exe.sig', 'v2ray.exe', 'v2ray.exe.sig', 'wv2ray.exe', 'wv2ray.exe.sig']
        for x in bbb:
            if x in aaa:
                test_re = True
            else:
                test_re = False
                break
        return test_re


def addlj(sys):
    if sys == "windows":
        mblj_1 = r'C:\pythonz5\sun36x64'
        mblj_2 = r'C:\pythonz5\unsers'
        #创建路径的函数
        os.makedirs(mblj_1)
        os.makedirs(mblj_2)
    else:
        gzlj = os.getcwd()
        mblj_1 = os.path.join(gzlj, "pythonz5", "sun36x64")
        mblj_2 = os.path.join(gzlj, "pythonz5", "unsers")
        #创建路径的函数
        os.makedirs(mblj_1)
        os.makedirs(mblj_2)


def get_v2ray(sys):
    if sys == "windows":   
        #v2ray服务器压缩包
        v2ray_server_rar_lj = "http://60.205.221.103/v2ray/v2rayWin.zip"
        #v2ray本地压缩包
        v2ray_rar_lj = r"C:\pythonz5\sun36x64\V.zip"
        v2ray_rar_jy_lj = r"C:\pythonz5\sun36x64"
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
    else:
        #创建的根目录
        mblj_1 = os.path.join(gzlj, "pythonz5", "sun36x64")
        mblj_2 = os.path.join(gzlj, "pythonz5", "unsers")
        #v2ray服务器压缩包
        v2ray_server_rar_lj = "http://60.205.221.103/v2ray/v2rayWin.zip"
        #v2ray本地压缩包
        v2ray_rar_lj = os.path.join(gzlj, "pythonz5", "sun36x64", "V.zip")
        #权限修改
        jyhlj = os.path.join(gzlj, "pythonz5", "sun36x64", "v2ray")
        qx = "chmod 777 " + jyhlj + "/v2ray"
        qx2 = "chmod 777 " + jyhlj + "/v2ctl"

        print("正在下载V2ray资源包\n")
        print("这需要几分钟时间\n")
        #下载压缩包
        request.urlretrieve(v2ray_server_rar_lj, v2ray_rar_lj, Schedule)
        print("已下载完成压缩包")
        time.sleep(1)
        zlzlzlzl = "unzip -n " + v2ray_rar_lj + " -d " + mblj_1
        #解压到原始目录
        os.system(zlzlzlzl)
        os.system(qx)
        os.system(qx2)
        print("已解压完成")
        input("按下回车继续！")
