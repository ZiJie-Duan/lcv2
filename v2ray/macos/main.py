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
import ssl 

from mods import install_v2,lod_del,tool_win,update,lod_del,user,s_server,X,strat_v2,Aaes
#https协议兼容
ssl._create_default_https_context = ssl._create_unverified_context


#程序入口
if __name__ == "__main__":
	#防止程序打包无限循环
	multiprocessing.freeze_support()