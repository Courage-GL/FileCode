"""
    创建两个线程 同时执行
    一个负责打印 1---52 52个数字
    另外一个线程打印A--Z 26个字母
    要求 12A34B
"""
from threading import Thread,Lock

lock01 = Lock()
lock02 =Lock()

def print_number():
    # rang(start,end,step)
    for i in range(1,53,2):
        lock01.acquire()
        print(i)
        print(i+1)
        lock02.release()

def print_char():
    for char in range(65,91):
        lock02.acquire()
        print(chr(char))
        lock01.release()

t1 = Thread(target=print_number)
t2 = Thread(target=print_char)
# 在线程开始之执行之前先阻塞 保证打印数字的线程先执行
lock02.acquire()
t1.start()
t2.start()
t1.join()
t2.join()

