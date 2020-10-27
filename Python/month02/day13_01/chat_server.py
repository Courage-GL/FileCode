"""
Author: Levi
Email: lvze@tedu.cn
Time:  2020-10-20
env: python3.6  pycharm
socket and Process exercise
"""
from socket import *
from multiprocessing import Process

# 服务器地址
HOST = "0.0.0.0"
PORT = 8000
ADDR = (HOST, PORT)

# 存储用户信息  {name:address}
user = {}


# 处理进入聊天室
def login(sock, name, addr):
    if name in user:
        # 反馈结果
        sock.sendto(b"FAIL", addr)
    else:
        sock.sendto(b"OK", addr)
        # 循环通知其他人
        msg = "欢迎 %s 进入聊天室" % name
        for i in user:
            sock.sendto(msg.encode(), user[i])
        user[name] = addr  # 增加该用户
    print(user)


# 程序启动函数
def main():
    # UDP套接字
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(ADDR)
    p = Process(target=request, args=(sock,))
    p.daemon = True
    p.start()
    while True:
        content = input("管理员消息：")
        if content == "exit":
            break
        msg = "CHAT 管理员消息 " + content
        sock.sendto(msg.encode(), ADDR)
    # p.join()


def request(sock):
    # 循环接收各种客户端请求 （总分模式）
    while True:
        # 接收所有客户端所有请求
        data, addr = sock.recvfrom(1024)
        # 对数据结构进行简单解析
        tmp = data.decode().split(' ', 2)
        if tmp[0] == "LOGIN":
            # tmp --> [LOGIN,name]
            login(sock, tmp[1], addr)
        elif tmp[0] == "CHAT":
            # 聊天函数
            chat(sock, tmp[1], tmp[2])
        elif tmp[0] == "EXIT":
            exit_chat(sock, tmp[1])


# 退出聊天室
def exit_chat(sock, name):
    del user[name]
    msg = "%s退出了聊天室" % name
    for i in user:
        sock.sendto(msg.encode(), user[i])


def chat(sock, name, content):
    msg = "%s:%s" % (name, content)
    for i in user:
        if i != name:
            sock.sendto(msg.encode(), user[i])


if __name__ == '__main__':
    main()
