# -- coding:utf-8--
from urllib import request
import socket


#服务器更新文件位置
update_exe_url = "http://60.205.221.103/v2ray/v2rayWinX.zip"
Win_up_exe_lj = os.path.join(gzlj, "v2rayWinX.zip")
Mac_up_exe_lj = os.path.join(gzlj, "Desktop", "v2rayMacX.zip")
update_bb = "5.1"


def get_update(sys):
    print("检测到更新！\n")
    print("正在下载更新！\n")
    if sys == "windows":
        #用于获取更新的函数
        request.urlretrieve(update_exe_url, Win_up_exe_lj)
    else:
        request.urlretrieve(update_exe_url, Mac_up_exe_lj)

def update(sys):
	#用于检查是否需要更新的函数
	sock = socket.socket()
        HOST = '60.205.221.103'
        PORT = 2233
        sock.connect((HOST, PORT))
        #发送模式
        sock.sendall("update".encode())
        #接受服务器的状态码
        server_s = sock.recv(1024).decode()
        sock.close()
    if server_s == update_bb:
        print("V" + update_bb)
    else:
        get_update(sys)
        if sys == "windows":
            print("新版本下载完成\n")
            print("请解压并运行 本文件根目录的‘v2rayWinX.zip’\n")
        else:
            print("新版本下载完成\n")
            print("请解压并运行 桌面的‘v2rayWinX.zip’\n")


        

