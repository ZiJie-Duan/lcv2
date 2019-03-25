#mac os
import os
import json

def relj():

	gzlj = os.path.realpath(__file__) 

	gzlist = gzlj.split("/")

	gzlist.remove("main.py")
	gzlist.remove("")


	gzlist.append("config.json")
	gzljx1 = "/".join(gzlist)
	gzljx2 = "/" + gzljx1

	return gzljx2

def read_config(filename):

'''
with open(filename,'w') as ojbk:
    json.dump(numbers,ojbk)
'''

with open(filename) as zx:
	pzwj = json.load(zx)

	user = pzwj["user"]
	



