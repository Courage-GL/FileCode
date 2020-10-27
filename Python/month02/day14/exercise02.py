"""
    练习2：创建两个线程 同事执行
    一个负责打印 1---52 52个数字
    另外一个线程打印A--Z 26个字母
    要求 12A34B
"""
from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()


def print_number():
    for number in range(1, 53, 2):
        lock1.acquire()
        print(number)
        print(number + 1)
        lock2.release()


def print_char():
    for number in range(65, 9):
        lock2.acquire()
        print(chr(number))
        lock1.release()


t1 = Thread(target=print_number)
t2 = Thread(target=print_char)

lock2.acquire()
t1.start()
t2.start()
t1.join()
t2.join()
