"""
    含有参数的进程函数示例
"""

from multiprocessing import Process
from time import sleep


# 含有参数的进程函数
def worker(sec, name):
    for i in range(3):
        sleep(sec)
        print("I'm % s" % name)
        print("I'm working")


if __name__ == '__main__':
    # 创建进程 args传参
    # p = Process(target=worker, args=(2, '小明'))
    # 创建进程 关键字传参
    # p = Process(target=worker,kwargs={'name': 'Tom', 'sec': 2})
    # 创建进程 两种传参方式一起用
    p = Process(target=worker, args=(2, ), kwargs={'name': 'Tom'})
    p.start()
    # 参数为超时时间 最多等待几秒
    # p.join(3)
    p.join()