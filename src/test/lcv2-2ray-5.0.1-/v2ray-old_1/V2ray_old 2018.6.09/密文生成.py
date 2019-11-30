# -- coding:utf-8--
import time

print("加密测试")

x = input("\n指令:")
y = input("参数：")

print("\n明文指令拆散")
xx = list(x)
print(xx)

print("\n时间数值")
timea = time.strftime("%Y%m%d%H")
print(timea)

timeb = str(timea)
times = list(timeb)
print("\n时间拆散值")
print(times)

szmwlb = []

XXX = int(times[-1]) * int(times[-2])
yy = int(y) ** int(y) + XXX +int(timea)

for zc in xx:
	if zc == "q":
		ys_1 = yy * 2
		szmwlb.append(ys_1)	
	if zc == "Q":
		ys_1 = yy ** 3
		szmwlb.append(ys_1)
		
	if zc == "w":
		ys_1 = yy * 4
		szmwlb.append(ys_1)
	if zc == "W":
		ys_1 = yy ** 5 
		szmwlb.append(ys_1)
		
	if zc == "r":
		ys_1 = yy * 6
		szmwlb.append(ys_1)
	if zc == "R":
		ys_1 = yy ** 7
		szmwlb.append(ys_1)
		
	if zc == "t":
		ys_1 = yy * 8
		szmwlb.append(ys_1)
	if zc == "T":
		ys_1 = yy ** 9
		szmwlb.append(ys_1)
		
	if zc == "y":
		ys_1 = yy * 10
		szmwlb.append(ys_1)
	if zc == "Y":
		ys_1 = yy ** 2
		szmwlb.append(ys_1)
		
	if zc == "u":
		ys_1 = yy * 11
		szmwlb.append(ys_1)
	if zc == "U":
		ys_1 = yy ** 3
		szmwlb.append(ys_1)
		
	if zc == "i":
		ys_1 = yy * 12
		szmwlb.append(ys_1)
	if zc == "I":
		ys_1 = yy ** 4
		szmwlb.append(ys_1)
		
	if zc == "o":
		ys_1 = yy * 13
		szmwlb.append(ys_1)
	if zc == "O":
		ys_1 = yy ** 5
		szmwlb.append(ys_1)
		
	if zc == "p":
		ys_1 = yy * 14
		szmwlb.append(ys_1)
	if zc == "P":
		ys_1 = yy ** 6
		szmwlb.append(ys_1)
		
	if zc == "e":
		ys_1 = yy * 15
		szmwlb.append(ys_1)
	if zc == "E":
		ys_1 = yy ** 7
		szmwlb.append(ys_1)
		
		
		
	if zc == "a":
		ys_1 = yy * 16
		szmwlb.append(ys_1)
	if zc == "A":
		ys_1 = yy ** 8
		szmwlb.append(ys_1)
		
	if zc == "s":
		ys_1 = yy * 17
		szmwlb.append(ys_1)
	if zc == "S":
		ys_1 = yy ** 9
		szmwlb.append(ys_1)
		
	if zc == "d":
		ys_1 = yy * 18
		szmwlb.append(ys_1)
	if zc == "D":
		ys_1 = yy ** 2
		szmwlb.append(ys_1)
		
	if zc == "f":
		ys_1 = yy * 19
		szmwlb.append(ys_1)
	if zc == "F":
		ys_1 = yy ** 3
		szmwlb.append(ys_1)
		
	if zc == "g":
		ys_1 = yy * 20
		szmwlb.append(ys_1)
	if zc == "G":
		ys_1 = yy ** 4
		szmwlb.append(ys_1)
		
	if zc == "h":
		ys_1 = yy * 21
		szmwlb.append(ys_1)
	if zc == "H":
		ys_1 = yy ** 5
		szmwlb.append(ys_1)
		
	if zc == "j":
		ys_1 = yy * 22
		szmwlb.append(ys_1)
	if zc == "J":
		ys_1 = yy ** 6
		szmwlb.append(ys_1)
		
	if zc == "k":
		ys_1 = yy * 23
		szmwlb.append(ys_1)
	if zc == "K":
		ys_1 = yy ** 7
		szmwlb.append(ys_1)
		
	if zc == "l":
		ys_1 = yy * 24
		szmwlb.append(ys_1)
	if zc == "L":
		ys_1 = yy ** 8
		szmwlb.append(ys_1)
		
		
		
		
	if zc == "z":
		ys_1 = yy * 25
		szmwlb.append(ys_1)
	if zc == "Z":
		ys_1 = yy ** 9
		szmwlb.append(ys_1)
		
	if zc == "x":
		ys_1 = yy * 26
		szmwlb.append(ys_1)
	if zc == "X":
		ys_1 = yy ** 2
		szmwlb.append(ys_1)
		
	if zc == "c":
		ys_1 = yy * 27
		szmwlb.append(ys_1)
	if zc == "C":
		ys_1 = yy ** 3
		szmwlb.append(ys_1)
		
	if zc == "v":
		ys_1 = yy * 28
		szmwlb.append(ys_1)
	if zc == "V":
		ys_1 = yy ** 4
		szmwlb.append(ys_1)
		
	if zc == "b":
		ys_1 = yy * 29
		szmwlb.append(ys_1)
	if zc == "B":
		ys_1 = yy ** 5
		szmwlb.append(ys_1)
		
	if zc == "n":
		ys_1 = yy * 30
		szmwlb.append(ys_1)
	if zc == "N":
		ys_1 = yy ** 6
		szmwlb.append(ys_1)
		
	if zc == "m":
		ys_1 = yy * 31
		szmwlb.append(ys_1)
	if zc == "M":
		ys_1 = yy ** 7
		szmwlb.append(ys_1)
		

print('\n一级密文列表')
print(szmwlb)

mwzh_3 = []

for mwzh in szmwlb:
	mwzh_1 = str(mwzh)
	mwzh_3.append(mwzh_1)
	
mw = ''.join(mwzh_3)
print("\n最终密文")
print(mw)

input('按下回车继续')