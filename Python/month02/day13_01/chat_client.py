"""
chat room 客户端代码
"""

from socket import *
from multiprocessing import Process
import sys

# 服务器地址
ADDR = ('119.3.124.77', 8000)


def login(sock):
    while True:
        # 进入聊天室
        name = input("Name:")
        # 发送姓名
        msg = "LOGIN " + name
        sock.sendto(msg.encode(), ADDR)
        # 接收结果
        result, addr = sock.recvfrom(128)
        if result.decode() == 'OK':
            print("进入聊天室")
            return name
        else:
            print("该用户已存在")


# 网络连接
def main():
    sock = socket(AF_INET, SOCK_DGRAM)
    # 为了确保客户端服务器地址不变化
    sock.bind(("0.0.0.0", 8023))
    name = login(sock)  # 进入聊天室
    p = Process(target=recv_msg, args=(sock,))
    # 父进程退出 子进程也跟着退出
    p.daemon = True
    p.start()
    send_msg(sock, name)
    # p.join()


# 接收消息
def recv_msg(sock):
    while True:
        data, addr = sock.recvfrom(1024 * 10)
        msg = "\n%s\n发言：" % data.decode()
        print(msg, end="")


# 发送消息
def send_msg(sock, name):
    while True:
        try:
            content = input("发言：")
        except KeyboardInterrupt:
            content = 'exit'
        if content == 'exit':
            msg = "EXIT " + name
            sock.sendto(msg.encode(), ADDR)
            sys.exit("您已退出聊天室")
        msg = "CHAT %s %s" % (name, content)
        sock.sendto(msg.encode(), ADDR)


if __name__ == '__main__':
    main()

