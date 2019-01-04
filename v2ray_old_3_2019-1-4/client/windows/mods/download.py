#!/usr/bin/python
#encoding:utf-8
import urllib
import os
def Schedule(a,b,c):
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print('%.2f%%' %(per))

url = "http://60.205.221.103/v2ray/v2rayWin.zip"
#local = url.split('/')[-1]
local = r"C:\Users\lucycore\Desktop\hi.zip"
urllib.request.urlretrieve(url, local, Schedule)
