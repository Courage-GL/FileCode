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
tickets = []
for i in range(1,501):
    tickets.append("T%d" % i)

def buying_tickets(name):
    # pop() 函数 默认从最后删除数据
    while tickets:
        print("%s窗口卖出了%s票"%(name, tickets.pop(0)))


jobs = []
for i in range(10):
    t = Thread(target=buying_tickets,args=("W%d" % i,))
    jobs.append(t)
    t.start()

for job in jobs:
    job.join()
