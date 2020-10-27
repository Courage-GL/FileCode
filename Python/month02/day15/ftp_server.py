"""
    FTP 文件服务器
    需求：
    【1】 分为服务端和客户端，要求可以有多个客户端同时操作。

    【2】 客户端可以查看服务器文件库中有什么文件。

    【3】 客户端可以从文件库中下载文件到本地。

    【4】 客户端可以上传一个本地文件到文件库。

    【5】 使用print在客户端打印命令输入提示，引导操作
"""
import socket
from signal import *
from multiprocessing import Process
import os

HOST = "0.0.0.0"
PORT = 12345
ADDR = (HOST, PORT)
# 文件库的位置
FTP = "work/"


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
        # 接收某一个客户端的操作
        data = tcpfd.recv(1024).decode()
        if data == "LIST":
            do_list(tcpfd)
        elif data == "DOWNLOAD":
            down_file(tcpfd)
            # print("下载")
        elif data == "UPLOAD":
           do_upload(tcpfd)
        elif data == "EXIT":
            break
        if not data:
            break
        print("客户端传来的消息---->", data)
    do_exit(tcpfd)


def do_exit(tcpfd):
    tcpfd.send("EXIT".encode())
    tcpfd.close()


def do_upload(tcpfd):
    data = tcpfd.recv(1024).decode()
    datalist = data.split("\n")
    if datalist[0] == "UPLOAD:":
        datalist.remove("UPLOAD:")
        print('\n%s\n文件即将开始拷贝' % datalist)
        if not os.path.exists("work2/"):
            os.mkdir("work2/")
        for file in datalist:
            with open(FTP + file, "rb") as old_file:
                with open("work2/" + file, "wb") as new_file:
                    for line in old_file:
                        new_file.write(line)
        print("文件拷贝完成")




def down_file(tcpfd):
    files = os.listdir(FTP)

    if not files:
        tcpfd.send("FTP列表里没有文件\n".encode())
    else:
        tcpfd.send("COPY:\n".encode())
        data = "\n".join(files)
        tcpfd.send(data.encode())


def do_list(tcpfd):
    files = os.listdir(FTP)
    if not files:
        tcpfd.send("FTP列表里没有文件\n".encode())
    else:
        # 用\n来拼接flies
        tcpfd.send("FILE:\n".encode())
        data = "\n".join(files)
        tcpfd.send(data.encode())


if __name__ == '__main__':
    main()
