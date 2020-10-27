"""
创建流程

【1】 将需要新进程执行的事件封装为函数

【2】 通过模块的Process类创建进程对象，关联函数

【3】 可以通过进程对象设置进程信息及属性

【4】 通过进程对象调用start启动进程

【5】 通过进程对象调用join回收进程资源
"""
import multiprocessing as mp
from time import sleep


# 进程的执行函数
def fun():
    print("OK,开始执行一个进程内容")
    sleep(3)
    print("OK,还得等3秒钟")


if __name__ == '__main__':
    # 创建进程对象 绑定函数
    p = mp.Process(target=fun)
    # 启动进程 这时进程产生 进程执行fun函数
    p.start()
    print("REPORT,我也要干点事情")
    sleep(2)
    print("OK,两秒钟我执行完了")
    # 阻塞等待回收进程  当函数执行完 关闭进程 将创建的进程资源释放
    p.join()