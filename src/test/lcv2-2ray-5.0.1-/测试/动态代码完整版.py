# -- coding:utf-8--
import multiprocessing
from urllib import request
import os
import shutil
import zipfile
import time
import datetime
import json
import sys
import socket
import uuid

# locals()
# join()

hi = "lucy.txt"

e = ""

mllb = []

zcml = []

with open(hi) as xxx:

	for hii in xxx:

		if hii == "~\n":

			e = "".join(zcml)
			mllb.append(e)
			zcml = []

		else:

			zcml.append(hii)

for ml in mllb:
	exec(ml)

input("")

"""
with open(hi) as xxx:
	for hii in xxx:
		mllb.append(hii)

a = "".join(mllb)
print(a)

print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")
print("-------------------------------------------")

exec(a)

input("")

a = 0
b = "bl"
c = ""
d = locals()
e = ""
"""
