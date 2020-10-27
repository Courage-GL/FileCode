"""
    多进程网络并发模型
"""

import socket
from multiprocessing import Process
from signal import *

HOST = "0.0.0.0"
PORT = 5678
ADDR = (HOST, PORT)


def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)
    print("LISTEN THE PORT %d" % PORT)
    # 处理僵尸进程
    signal(SIGCHLD, SIG_IGN)
    while True:
        # 强制退出
        try:
            # 循环接收客户端连接
            tcpfd, addr = sock.accept()
            print("CONNECTION FROM CLIENT", addr)
        except KeyboardInterrupt:
            sock.close()
            break
        # 为连接的客户端创建新进程
        p = Process(target=handle, args=(tcpfd,))
        # 子进程也跟着退出
        p.daemon = True
        p.start()


# 实现具体的业务逻辑 客户端请求都在这里处理
def handle(tcpfd):
    while True:
        data = tcpfd.recv(1024)
        if not data:
            break
        print("客户端传来的消息---->", data.decode())
        # tcp 发送消息不用地址 udp需要使用
        tcpfd.send("服务器收到请求-le".encode())
    tcpfd.close()


if __name__ == '__main__':
    main()
