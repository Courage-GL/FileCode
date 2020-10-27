"""
    多线程网络并发模型
"""

import socket
from threading import Thread

HOST = "0.0.0.0"
PORT = 12345
ADDR = (HOST, PORT)


class MyThread(Thread):
    def __init__(self,tcpcnf):
        self.tcpfd = tcpcnf
        super().__init__()

    # 实现具体的业务逻辑 客户端请求都在这里处理
    def run(self):
        while True:
            data = self.tcpfd.recv(1024)
            if not data:
                break
            print("客户端传来的消息---->", data.decode())
            # tcp 发送消息不用地址 udp需要使用
            self.tcpfd.send("服务器收到请求-le".encode())
        self.tcpfd.close()

def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.bind(ADDR)
    sock.listen(5)
    print("LISTEN THE PORT %d" % PORT)
    while True:
        # 强制退出
        try:
            # 循环接收客户端连接
            tcpfd, addr = sock.accept()
            print("CONNECTION FROM CLIENT", addr)
        except KeyboardInterrupt:
            # 关闭套接字
            sock.close()
            break
        # 为连接的客户端创建线程
        t = MyThread(tcpfd)
        # 子进程也跟着退出
        t.setDaemon(True)
        t.start()





if __name__ == '__main__':
    main()
