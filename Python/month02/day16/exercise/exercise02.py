"""
    基于poll的 IO并发模型
"""
from socket import socket
from select import *
map={}
sock = socket()
sock.bind(("0.0.0.0",23456))
sock.listen()
sock.setblocking(False)
p = poll()
map[sock.fileno()] = sock
p.register(sock,POLLIN)
while True:
    events = p.poll()
    for fileno,event in events:
        if fileno==sock.fileno():
            tcpconn, addr = map[fileno].accept()
            tcpconn.setblocking(False)
            map[tcpconn.fileno()] =tcpconn
            p.register(tcpconn,POLLIN)
        elif event==POLLIN:
            data = map[fileno].recv(1024).decode()
            if not data:
                p.unregister(map[fileno])
                map[fileno].close()
                del map[fileno]
                continue
            print("客户端传来消息",data)
            p.register(map[fileno],POLLOUT)
        elif event==POLLOUT:
             map[fileno].send("OK".encode())
             # poll特征 用完了不移除 而是转化为 读
             p.register(map[fileno],POLLIN)