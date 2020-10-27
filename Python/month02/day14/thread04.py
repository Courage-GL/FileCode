"""
    自定义线程类
    继承Thread类
    重写__init__方法添加自己的属性 使用super()加载父类属性
    重写run方法
"""
from threading import Thread
from time import sleep

class NewThread(Thread):
    def __init__(self,name):
        self.name1 = name
        super().__init__()

    def run(self):
        for i in range(3):
            sleep(3)
            print("自定义线程", self.name1)

new_thread = NewThread("new_thread")
new_thread.start()
new_thread.join()

