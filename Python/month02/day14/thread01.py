from threading import Thread
from time import sleep


def fun01():
    for i in range(3):
        sleep(1)
        print("播放：粉红色的回忆")


t = Thread(target=fun01)
t.setName("new_thread")
t.start()
print(t.is_alive())
print(t.getName())
for i in range(4):
    sleep(1)
    print("播放：葫芦娃")
t.join()
print(t.is_alive())
