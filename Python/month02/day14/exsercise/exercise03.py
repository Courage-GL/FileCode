"""
    杨子荣拜山头
"""

from threading import Thread, Event, Lock

msg = None
e = Event()
lock =Lock()


def yangzirong():
    # 也可以通过lock 使得线程里的代码先执行
    lock.acquire()
    print("拜山头")
    global msg
    msg = "天王盖地虎"
    lock.release()
    # e.set()


t = Thread(target=yangzirong)
t.start()
# 由于线程是抢cpu来执行的 所以 不确定到底是哪个先执行的
# 可以通过wait来阻塞 让线程先执行
# e.wait()

if msg == "天王盖地虎":
    print("宝塔镇河妖")
    print("是自己人，来坐。")
else:
    print("不是自己人，弄出去杀了。")
    print("卧槽，无情哈拉少。")
t.join()
