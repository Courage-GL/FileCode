"""
    练习：模拟一个售票系统程序
    一共500张票 ---》T1-T500
    编程10个线程模拟10个售票窗口机器 记为W1-W10
    10个窗口同时售票 直到所有的票买完

    票按照顺序出售
    每个窗口卖出一张票 w2----T345
    买一张票需要0.1s
"""
from threading import Thread
from time import sleep

ticks = []
for i in range(1, 501):
    ticks.append("T%d" % i)


def buy_ticket(name):
    while ticks:
        print("%s<--->%s" % (name, ticks.pop(0)))
        sleep(0.1)


jobs = []
for i in range(10):
    thread = Thread(target=buy_ticket, args=("W%d" % i,))
    thread.start()
    jobs.append(thread)

for job in jobs:
    job.join()
