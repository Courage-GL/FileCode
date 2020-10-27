"""
    练习1 大文件拆分
    将一个文件拆分成两个部分 按照字节数平分
"""
from multiprocessing import Process
import os
from signal import *


def split_file(file_name):
    with open('dict.txt', 'rb') as file:
        size = os.path.getsize('dict.txt') // 2
        with open(file_name, 'wb') as a1:
            if size >= 1024:
                a1.write(file.read(1024))
                size -= 1024
            else:
                a1.write(file.read(size))


def split_file1(file_name):
    with open('dict.txt', 'rb') as file:
        size = os.path.getsize('dict.txt') // 2
        file.seek(size, 0)
        with open(file_name, 'wb') as a1:
            for line in file:
                a1.write(line)


if __name__ == '__main__':
    # 忽略子进程退出 
    # signal(SIGCHLD, SIG_IGN)
    p = Process(target=split_file, args=('a.txt',))
    p1 = Process(target=split_file1, args=('b.txt',))
    p.start()
    p1.start()

    # 阻塞函数
    p.join()
    p1.join()
