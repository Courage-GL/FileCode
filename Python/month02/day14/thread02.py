from threading import Thread
from time import sleep


def function(time, name):
    sleep(time)
    print(name)


jobs = []

for i in range(5):
    t = Thread(target=function, args=(2, "T%d" % i))
    jobs.append(t)
    t.start()

for job in jobs:
    job.join()
