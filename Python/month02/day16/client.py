"""
    TCP客户端
"""
import socket
import sys
import os
from time import sleep

HOST = "127.0.0.1"
PORT = 23456
ADDRESS = (HOST, PORT)


def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.connect(ADDRESS)
    while True:
        order = input("消息：")
        if not order:
            break
        sock.send(order.encode())
        print("服务端返回", sock.recv(1024).decode())


if __name__ == '__main__':
    main()
