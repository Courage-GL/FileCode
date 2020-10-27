"""
    基于 epoll的 IO并发模型
"""
from socket import *
from select import *

map = {}
sock = socket()
sock.bind(("0.0.0.0", 23456))
sock.listen(5)
sock.setblocking(False)
ep = epoll()
map[sock.fileno()] = sock
ep.register(sock, EPOLLIN)
while True:
    events = ep.poll()
    for fileno, event in events:
        if fileno == sock.fileno():
            tcpconnfd, addr = map[fileno].accept()
            tcpconnfd.setblocking(False)
            map[tcpconnfd.fileno()] = tcpconnfd
            ep.register(tcpconnfd, EPOLLIN)
        elif event == EPOLLIN:
            data = map[fileno].recv(1024).decode()
            if not data:
                ep.unregister(map[fileno])
                map[fileno].close()
                del map[fileno]
                continue
            print(data)
            # map[fileno].send("OK".encode())
            ep.register(map[fileno], EPOLLIN)
        elif event == EPOLLOUT:
            map[fileno].send("OK".encode())
            ep.unregister(map[fileno])
            ep.register(map[fileno], EPOLLIN)
