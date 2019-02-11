import json
import uuid
from mods import aess
import os

def w_id(uuid):
	#生成uuid
	#加密后的id列表
	adm_id = []
	#拆分id
	fg_uuid = str(uuid).split("-")

	#循环加密id
	for x in fg_uuid:
		y = Aaes.adm("lucycore",x)
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
