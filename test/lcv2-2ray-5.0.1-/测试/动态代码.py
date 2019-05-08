lj = "core.txt"

print("正在读取文件代码")
with open(lj) as xxx:    
    for hii in xxx: 
        print(hii)
        exec(hii)


#exec()