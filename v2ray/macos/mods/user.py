import json
import uuid
from mods import aess
import os
import sys

def w_id(uuid):
	#生成uuid
	#加密后的id列表
	adm_id = []
	#拆分id
	fg_uuid = str(uuid).split("-")

	#循环加密id
	for x in fg_uuid:
		y = aess.adm("lucycore",x)
		adm_id.append(y)

	gzlj = os.getcwd()
	user = os.path.join(gzlj, "pythonz5.1","unsers","user.json")
	
	with open(user,'w') as ojbk_1:
		json.dump(adm_id,ojbk_1)


def b_id():
	uid = uuid.uuid4()
	return uid


def d_id():
	gzlj = os.getcwd()
	user = os.path.join(gzlj, "pythonz5.1","unsers","user.json")
	os.remove(user)


def read_user():
	#明文列表
	mwlb = []
	gzlj = os.getcwd()
	user = os.path.join(gzlj, "pythonz5.1","unsers","user.json")
	#打开用户文件
	with open(user) as zx:
		userlb = json.load(zx)
	#循环解密用户uuid
	for x in userlb:
		mw = aess.jm("lucycore",x)
		mwlb.append(mw)

	mwzfc = ''.join(mwlb)
	return mwzfc


def uid_cl(uuid):
	#用于将uuid去除中间连字符的函数
	fg_uuid = str(uuid).split("-")
	zfc = ''.join(fg_uuid)
	return zfc





