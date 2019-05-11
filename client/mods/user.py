# -- coding:utf-8--
import json

def read_user(lj):

	with open(lj) as zx:
		userid = json.load(zx)

	return userid


def write_user(lj,uid):

	with open(lj,'w') as ojbk:
		json.dump(uid,ojbk) 

