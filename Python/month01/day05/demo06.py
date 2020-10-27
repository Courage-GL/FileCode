"""
    列表嵌套内存图
        浅拷贝

"""
list01 = [10, [20, 30]]
list02 = list01[:]# 浅拷贝：复制一层数据
list01[0] = 100# 修改第一层数据,互不影响（2份）
list01[1][0] = 200 #修改深层数据,互相影响（1份）
print(list02) # [10, [200, 30]]
