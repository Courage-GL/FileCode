"""
    同时创建多个子进程
"""
from multiprocessing import Process
from time import sleep
import os, sys


def th1():
    sleep(3)
    print("吃饭")
    print(os.getppid(), '<-------->', os.getpid())


def th2():
    sleep(4)
    print("睡觉")
    print(os.getppid(), '<-------->', os.getpid())


def th3():
    sys.exit("打豆豆进程退出。。。。")
    sleep(5)
    print("打豆豆")
    print(os.getppid(), '<-------->', os.getpid())


if __name__ == '__main__':

    things = [th1, th2, th3]
    jobs = []  # 存储进程对象

    for th in things:
        p = Process(target=th)
        jobs.append(p)
        p.start()

    for job in jobs:
        job.join()
