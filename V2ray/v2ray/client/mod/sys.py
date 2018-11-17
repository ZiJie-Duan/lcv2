
def test_sys():
    #用于测试系统的函数
    import os

    way = "C:\\Windows"
    result = ""

    if os.path.exists(way):
        result = "windows"
    else:
        result = "mac os"

    return result

