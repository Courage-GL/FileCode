"""
    进程属性信息 解释
"""

from multiprocessing import Process
import time


def fun():
    for i in range(2):
        print(time.ctime())
        time.sleep(2)


if __name__ == '__main__':
    p = Process(target=fun, name='Aid')
    # 设置子进程随着父进程的退出而退出 start前设置
    p.daemon = True
    p.start()
    # 名字
    print('Name', p.name)
    # pid
    print('pid', p.pid)
    # 是否在进程生命周期内
    print('is alive', p.is_alive())
    # p.join()
