import uuid

uidlist = []

keyn = input("卡密数量：")
time = input("卡密时间：")

for x in range(int(keyn)):
	a = []
	b = uuid.uuid4()
	a.append(str(b))
	a.append(time)

	uidlist.append(a)

print(uidlist)
print("\n\n\n")
js = 0
for x,y in 	uidlist:
	js += 1
	print(str(js) + " " + x)