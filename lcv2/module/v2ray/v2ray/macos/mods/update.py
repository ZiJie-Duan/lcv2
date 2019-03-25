# -- coding:utf-8--
from urllib import request
import socket
import os


def Schedule(a,b,c):
    #显示进度的函数
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' %(per))


def get_update():
    gzlj = os.getcwd()
    Mac_up_exe_lj = os.path.join(gzlj, "Desktop", "v2rayWinX.zip")
    update_exe_url = "http://60.205.221.103/v2ray/v2rayWinX.zip"
    print("检测到更新！\n")
    print("正在下载更新！\n")

    #用于获取更新的函数
    request.urlretrieve(update_exe_url, Mac_up_exe_lj, Schedule)

def update():
    update_bb = "5.1"
    #用于检查是否需要更新的函数
    sock = socket.socket()
    HOST = '10.10.1.58'
    PORT = 2233
    sock.connect((HOST, PORT))
    #发送模式
    sock.sendall("update".encode())
    #接受状态
    server_s = sock.recv(1024).decode()
    print(server_s)
    if server_s == update_bb:
        print("V" + update_bb)
    else:
        get_update()

        print("新版本下载完成\n")
        print("请解压并运行 桌面的‘v2rayWinX.zip’\n")
        input("按下回车退出程序")
        sys.exit(0)



