# -- coding:utf-8--
from su.aes import encrypt, decrypt
import multiprocessing
from urllib import request
import mods
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import uuid


user = {}

zlb = []

username = "lucycore"
password = "killyou3000"
time = "0000-00-00-00-00"
Mac_1 = "78:4f:43:98:c3:8c"
IP = "192.168.1.1"

zlb = [password,time,IP,Mac_1]


user[username] = zlb

print(user)

fw = user[username]

print(fw)

def put_key(a):
	#用于输出密钥文件的函数
	#写入json 加密后的密钥
	with open("user",'w') as ls:
		json.dump(zlb,ls)




