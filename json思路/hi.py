import json

keyklj = "key.json"
userklj = "userk.json"

key = input("请输入您的密钥：")

with open(userklj) as zx_1:
	userk = json.load(zx_1)

with open(keyklj) as zx:
	keyk = json.load(zx)

if key in keyk.keys():
	time = keyk[key]
	print("您的密钥现已激活 时间：" + str(time))

	userk[key] = keyk[key]
	with open(userklj,'w') as ojbk:
		json.dump(userk,ojbk)
	print("写入完成！")

	del keyk[key]
	print(keyk)

	with open(keyklj,'w') as ojbk_1:
		json.dump(keyk,ojbk_1)
	print("删除完成！")

else:
	if key in userk.keys():
		usertime = userk[key]
		print("您已注册！并已激活！剩余时间：" + str(usertime))
		input("")
	else:
		print("抱歉您输入的密钥错误！")
		input("")
