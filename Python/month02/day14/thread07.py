"""
    LOCK 线程锁
"""
from threading import Thread, Lock

lock = Lock()
a = b = 0


def value():
    while True:
        with lock:
            if a != b:
                print("a=%d,b=%d" % (a, b))


t = Thread(target=value)
t.start()
while True:
    lock.acquire()  # 上锁
    a += 1
    b += 1
    lock.release()  # 解锁
t.join()
