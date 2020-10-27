"""
    非阻塞IO
"""

import socket
from time import *

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)

sock.bind(("0.0.0.0",12345))
sock.listen(5)
# 设置非阻塞
# sock.setblocking(False)
# 设置超时检测
sock.settimeout(2)
f = open("log.txt","a")
while True:
    try:
        c,addr= sock.accept()
    except socket.timeout as e:
        print("开始写日志")
        sleep(2)
        msg = "%s:%s\n" % (ctime(), e)
        f.write(msg)
        f.flush()
    except BlockingIOError as e:
        print("开始写日志")
        sleep(2)
        msg = "%s:%s\n" %(ctime(), e)
        f.write(msg)
        f.flush()

    else:
        data = c.recv(1024)
        print(data.decode())