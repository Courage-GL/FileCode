"""
    t.setName() 设置线程名称

    t.getName() 获取线程名称

    t.is_alive() 查看线程是否在生命周期

    t.setDaemon() 设置daemon属性值

    t.isDaemon() 查看daemon属性值

    daemon为True时主线程退出分支线程也退出。要在start前设置，通常不和join一起使用。
"""
from time import sleep
from threading import Thread


def fun():
    sleep(3)
    print("线程属性设置")


t = Thread(target=fun)
t.setName("new_thread")
print(t.is_alive())
# t.setDaemon(True)
t.start()
print(t.getName())
t.join()

#
# class Person:
#     def __init__(self, age):
#         self.__age = age
#
#
#     # @property
#     # def age(self):
#     #     return self.__age
#     #
#     # @age.setter
#     # def age(self, value):
#     #     self.__age = value
#
#
# Lily = Person(18)
#
# print(Lily.age)
