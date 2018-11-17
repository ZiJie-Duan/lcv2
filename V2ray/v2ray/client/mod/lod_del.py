# -- coding:utf-8--
import multiprocessing
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import uuid


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


def old_rm(sys):

    if sys == "windows":
        #检测第一代程序
        one_old_az_lj = r"C:\pythonX"
        if os.path.exists(one_old_az_lj):
            print("检测到旧版本的v2ray\n")
            print("第一代v2ray启动器！")
            print("正在卸载v2ray\n")
            try:
                remove_dir(one_old_az_lj)
            except:
                print("删除失败！")
                #删除错误反馈
                print("错误！X002\n")
                input("按下任意键退出程序！")
                sys.exit(0)
            print("删除完成!\n")

        #检测第二代程序
        one_old_az_lj = r"C:\pythonz"
        if os.path.exists(one_old_az_lj):
            print("检测到旧版本的v2ray\n")
            print("第二代v2ray启动器！")
            print("正在卸载v2ray\n")
            try:
                remove_dir(one_old_az_lj)
            except:
                print("删除失败！")
                #删除错误反馈
                print("错误！X002\n")
                input("按下任意键退出程序！")
                sys.exit(0)
            print("删除完成!\n")

        #检测第四代程序
        one_old_az_lj = r"C:\pythonz4"
        if os.path.exists(one_old_az_lj):
            print("检测到旧版本的v2ray\n")
            print("第四代v2ray启动器！")
            print("正在卸载v2ray\n")
            try:
                remove_dir(one_old_az_lj)
            except:
                print("删除失败！")
                #删除错误反馈
                print("错误！X002\n")
                input("按下任意键退出程序！")
                sys.exit(0)
            print("删除完成!\n")
    else:
        #工作路径
        gzlj = os.getcwd()
        #old路径
        old_python_1 = os.path.join(gzlj, "pythonX")
        old_python_2 = os.path.join(gzlj, "pythonz")
        old_python_4 = os.path.join(gzlj, "pythonz4")
        #检测第一代程序
        one_old_az_lj = os.path.join(old_python_1)
        if os.path.exists(one_old_az_lj):
            print("检测到旧版本的v2ray\n")
            print("第一代v2ray启动器！")
            print("正在卸载v2ray\n")
            try:
                remove_dir(one_old_az_lj)
            except:
                print("删除失败！")
                #删除错误反馈
                print("错误！X002\n")
                input("按下任意键退出程序！")
                sys.exit(0)
            print("删除完成!\n")

        #检测第二代程序
        one_old_az_lj = os.path.join(old_python_2)
        if os.path.exists(one_old_az_lj):
            print("检测到旧版本的v2ray\n")
            print("第二代v2ray启动器！")
            print("正在卸载v2ray\n")
            try:
                remove_dir(one_old_az_lj)
            except:
                print("删除失败！")
                #删除错误反馈
                print("错误！X002\n")
                input("按下任意键退出程序！")
                sys.exit(0)
            print("删除完成!\n")

        #检测第四代程序
        one_old_az_lj = os.path.join(old_python_4)
        if os.path.exists(one_old_az_lj):
            print("检测到旧版本的v2ray\n")
            print("第四代v2ray启动器！")
            print("正在卸载v2ray\n")
            try:
                remove_dir(one_old_az_lj)
            except:
                print("删除失败！")
                #删除错误反馈
                print("错误！X002\n")
                input("按下任意键退出程序！")
                sys.exit(0)
            print("删除完成!\n")
