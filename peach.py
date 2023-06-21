def addNum(a, b):
    return a+b

# 写一个函数读取csv文件 一行一行返回一个list

def readCsv(path): 
    with open(path, 'r') as f:
        lines = f.readlines()
        return lines

        