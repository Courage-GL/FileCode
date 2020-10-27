"""
    聊天室客户端
"""
import socket
from multiprocessing import Pool
from time import sleep

HOST = '127.0.0.1'
PORT = 3306
ADDR = (HOST, PORT)


def get_msg(socket):
    data, address = socket.recvfrom(1024)
    if data == 'OK'.encode():
        print("加入聊天室成功")
    elif data == 'CHAT'.encode():
        print("发送聊天信息成功")
    elif data == 'EXIT'.encode():
        print("退出聊天室成功")
    else:
        print(data.decode())


if __name__ == '__main__':
    # UDP套接字
    my_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)

    while True:
        pool = Pool()
        pool.apply_async(func=get_msg,
                         args=(my_socket,))
        pool.close()
        # pool.join()
        name = input(">>>>>")
        my_socket.sendto(name.encode(), ADDR)
