"""
    自定义进程类
    练习1： 使用进程池完成  文件拷贝 拷贝一个指定的目录（文件夹里全是普通文件，没有子文件夹）
    思考：1.什么事情作为进程池事件
        2.拷贝文件函数
"""
from multiprocessing import Pool
import os


def copy_file(file_name):
    with open(file_name, 'rb') as file:
        with open('copy/' + file_name.split('/')[1], 'wb') as new_file:
            for line in file:
                new_file.write(line)
            print(file_name.split('/')[1]+'拷贝完成')


if __name__ == '__main__':
    if not os.path.exists('copy'):
        os.mkdir('copy')
    pool = Pool()
    list_txt = os.listdir('text')
    for i in list_txt:
        pool.apply_async(func=copy_file, args=('text/' + i,))
    pool.close()
    pool.join()
