import json
import uuid
import Aaes

def test_user_f():
	zt = True
	user_id = ""
	user_lb = []
	user = r'C:\pythonz5\unsers\user.json'
	try:
		with open(user) as zx:
			us_id = json.load(zx)
		zt = True
		for x in us_id:
			y = Aaes.jm("lucycore",x)
			user_lb.append(y)
		user_id = "-".join(user_lb)

	except:
		zt = False
		user_id = "XXXXX"
	return zt, user_id


def write_user_id():
	#加密后的id列表
	adm_id = []
	#生成id
	uid = uuid.uuid4()
	print("您的ID：" + uid)
	#拆分id
	fg_uuid = str(uid).split("-")

	#循环加密id
	for x in fg_uuid:
		y = Aaes.adm("lucycore",x)
		adm_id.append(y)

	user = r'C:\pythonz5\unsers\user.json'
	
	with open(user,'w') as ojbk_1:
		json.dump(adm_id,ojbk_1)


'''

def userk_xr(mac,key,time):
	root = False
	x = "0"
	#用于添加用户的函数
	userklj = "userk.json"

	with open(userklj) as zx:
		userzd = json.load(zx)

	zhlb = [key,time,root,x]

	userzd[mac] = zhlb

	with open(userklj,'w') as ojbk_1:
		json.dump(userzd,ojbk_1)
'''