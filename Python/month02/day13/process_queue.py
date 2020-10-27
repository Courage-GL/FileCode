"""
    消息队列
"""
from multiprocessing import Process, Queue


def request(q):
    name = 'Levi'
    password = '123456'
    q.put(name)
    q.put(password)


def handle(q):
    name = q.get()
    password = q.get()
    print("NAME---->", name)
    print("PASSWORD----->", password)


if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=request, args=(q,))
    p2 = Process(target=handle, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    q.close()
