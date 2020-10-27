"""
    基于EPOLL的 IO网络并发模型
    IO 多路复用与非阻塞搭配
    重点代码！！！
"""
from socket import socket
from select import *

map = {}
HOST = "0.0.0.0"
PORT = 12346
ADDR = (HOST, PORT)
sock = socket()
sock.bind(ADDR)
sock.listen(5)
# 设置非阻塞
sock.setblocking(False)

p = epoll()
p.register(sock, EPOLLIN | EPOLLERR)
map[sock.fileno()] = sock

# 循环监控IO对象
while True:
    # 到这里阻塞监控
    events = p.poll()
    # fd 文件描述符 event是准备就绪的事件类型 真正的事件对象在map里存放着
    for fd, event in events:
        # 有客户端连接
        if fd == sock.fileno():
            connfd, addr = map[fd].accept()
            # 设置为非阻塞状态
            connfd.setblocking(False)
            # 将连接套接字也放到rlist里面
            p.register(connfd, EPOLLIN | EPOLLERR)
            map[connfd.fileno()] = connfd
        elif event == EPOLLIN:
            # 客户端发消息 connfd就绪
            data = map[fd].recv(1024).decode()
            # 客户端退出的处理
            if not data:
                p.unregister(fd)
                map[fd].close()
                del map[fd]
                continue
            print("客户端传过来" + data)
            map[fd].send("OK".encode())
        # print(map)
