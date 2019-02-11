# -- coding:utf-8--
import os
#工作路径
gzlj = os.getcwd()


def remove_dir(dir):
	#用于删除路径的函数
	dir = dir.replace('\\', '/')
	if(os.path.isdir(dir)):
		for p in os.listdir(dir):
			remove_dir(os.path.join(dir,p))
		if(os.path.exists(dir)):
			os.rmdir(dir)
	else:
		if(os.path.exists(dir)):
			os.remove(dir)


def old_rm():

    #检测第一代程序
    one_old_az_lj = os.path.join(gzlj,"pythonX")
    if os.path.exists(one_old_az_lj):
        print("检测到旧版本的v2ray\n")
        print("第一代v2ray启动器！")
        print("正在卸载v2ray\n")
        try:
            remove_dir(one_old_az_lj)
        except:
            print("删除失败！")
            #删除错误反馈
            print("错误！X002\n")
            input("按下任意键退出程序！")
            sys.exit(0)
        print("删除完成!\n")

    #检测第二代程序
    one_old_az_lj = os.path.join(gzlj,"C:\pythonz")
    if os.path.exists(one_old_az_lj):
        print("检测到旧版本的v2ray\n")
        print("第二代v2ray启动器！")
        print("正在卸载v2ray\n")
        try:
            remove_dir(one_old_az_lj)
        except:
            print("删除失败！")
            #删除错误反馈
            print("错误！X002\n")
            input("按下任意键退出程序！")
            sys.exit(0)
        print("删除完成!\n")

    #检测第四代程序
    one_old_az_lj = os.path.join(gzlj,"C:\pythonz4")
    if os.path.exists(one_old_az_lj):
        print("检测到旧版本的v2ray\n")
        print("第四代v2ray启动器！")
        print("正在卸载v2ray\n")
        try:
            remove_dir(one_old_az_lj)
        except:
            print("删除失败！")
            #删除错误反馈
            print("错误！X002\n")
            input("按下任意键退出程序！")
            sys.exit(0)
        print("删除完成!\n")

    #检测第五代程序
    one_old_az_lj = os.path.join(gzlj,"C:\pythonz5")
    if os.path.exists(one_old_az_lj):
        print("检测到旧版本的v2ray\n")
        print("5.0版本 v2ray启动器！")
        print("正在卸载v2ray\n")
        try:
            remove_dir(one_old_az_lj)
        except:
            print("删除失败！")
            #删除错误反馈
            print("错误！X002\n")
            input("按下任意键退出程序！")
            sys.exit(0)
        print("删除完成!\n")
