"""
    进程池使用范例
    * 如果主进程 或者父进程退出了 线程池会自动销毁
"""

from multiprocessing import Pool
from time import sleep, ctime
import random


# 事件函数
def worker(msg, sec):
    print(ctime(), '<--------------->', msg)
    sleep(sec)


if __name__ == '__main__':
    # 创建进程池
    pool = Pool()
    # 向线程池添加事件
    for i in range(10):
        msg = 'Tedu-%d' % i
        pool.apply_async(func=worker,
                         args=(msg, random.randint(1, 4)))

    # 关闭进程池 回收线程池里的进程
    pool.close()
    pool.join()
