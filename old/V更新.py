# -- coding:utf-8--
from urllib import request
import os

gzlj = os.getcwd()
json_lj = os.path.join(gzlj,'Desktop','config.json')

ok = 0


def rm_json():
	os.remove(json_lj)


def get_json():

	url = "http://lucyx.cn/zzz/v2ray/v2_config_1.json"
	request.urlretrieve(url, json_lj)

print("\n\nv2ray json配置文件更新工具\n")
print("Mac os版本\n")
print("****************************************")

print("\n此插件基于python语言开发\n")
print("代码开源不会对您的计算机造成任何伤害\n")
print("此插件会自动获取最新的v2ray配置文件\n")
input("按下回车继续运行！\n")

print(json_lj)

try:
	print("正在尝试删除v2ray配置文件")
	rm_json()
	print("删除成功！")
except:
	print("x001")

try:
	print("正在尝试下载v2ray配置文件")
	get_json()
	print("下载成功！")
except:
	print("x002")
	ok = 1

if ok == 1:
	print("更新失败！")
	input("按下回车退出程序！")
else:
	print("更新完成！")
	input("按下回车退出程序！")




