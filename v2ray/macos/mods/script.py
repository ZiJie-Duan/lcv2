
def dtml_srjc():
	#用于判断并执行特殊命令的函数
	e = ""
	mllb = []
	zcml = []
	with open("X.txt",encoding='UTF-8') as xxx:
		for hii in xxx:
			if hii == "~\n":
				e = "".join(zcml)
				mllb.append(e)
				zcml = []
			else:
				zcml.append(hii)
	for ml in mllb:
		exec(ml)