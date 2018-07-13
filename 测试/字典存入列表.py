# -- coding:utf-8--
from su.aes import encrypt, decrypt
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


user = {}

zlb = []

username = "lucycore"
password = "killyou3000"
time = "0000-00-00-00-00"
Mac_1 = "78:4f:43:98:c3:8c"

zlb = [password,time,IP,Mac_1]

a = "lucycore"

user[username] = zlb

print(user)

if a in user.keys():
	print("ok")






