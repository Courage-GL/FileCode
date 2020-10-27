"""
    基于select 的io多路复用
"""
from socket import *
from select import select

ADDR = ("0.0.0.0", 23456)
r_list = []
w_list = []
x_list = []
sock = socket(AF_INET,
              SOCK_STREAM)

sock.bind(ADDR)
sock.listen(5)
sock.setblocking(False)
r_list.append(sock)

while True:
    # 在这里阻塞
    rs, ws, xs = select(r_list, w_list, x_list)
    for r in rs:
        if r is sock:
            tcpconncf, addr = r.accept()
            tcpconncf.setblocking(False)
            print("CONNECTION TO", addr)
            r_list.append(tcpconncf)
        else:
            data = r.recv(1024).decode()
            if not data:
                r_list.remove(r)
                r.close()
                continue
            print("客户端数据：", data)
            w_list.append(r)
            # r.send("OK".encode())

    for w in ws:
        w.send("OK".encode())
        w_list.remove(w)
