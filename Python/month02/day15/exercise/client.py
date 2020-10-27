"""
    TCP客户端
"""
import socket
import sys
import os
from time import sleep

HOST = "127.0.0.1"
PORT = 12345
ADDRESS = (HOST, PORT)
COPY_DIR = "work/"


def exit_system(sock):
    sock.send("EXIT".encode())
    sock.close()
    sys.exit("谢谢使用")


def download_file(sock,file):
    send_msg = "GET "+file
    sock.send(send_msg.encode())
    msg = sock.recv(1024)
    if msg == "OK".encode():
        if not os.path.exists(COPY_DIR):
            os.mkdir(COPY_DIR)
        new_file = open(COPY_DIR + "new_file.txt", "wb")
        while True:
            data = sock.recv(1024)
            if data == "##".encode():
                break
            new_file.write(data)
    else:
        print("服务端文件不存在")


def put_file(connfd, file):
    # 测一下这个文件是否存在
    try:
        f = open(file, 'rb')
    except:
        print("客户端文件不存在")
        return
    else:
        # 防止file带有文件路径，提取文件名
        filename = file.split("/")[-1]
        data = "PUT " + filename
        connfd.send(data.encode())  # 发请求
        result = connfd.recv(128).decode()  # 等待回复
        if result == 'OK':
            # 上传文件 读--》发送
            while True:
                data = f.read(1024)
                if not data:
                    break
                connfd.send(data)
            sleep(0.1)
            connfd.send(b"##")
            f.close()
        else:
            print("服务端该文件已存在")



def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
    sock.connect(ADDRESS)
    while True:
        print("""
              ============ 命令选项 =============
                            LIST 
                          GET  file
                          PUT  file
                            EXIT
              ==================================
              """)

        order = input("请输入命令：")

        if not order or order == "EXIT":
            exit_system(sock)
        elif order == "LIST":
            get_file_list(sock)
        elif order[:3] == "GET":
            # 以空格分割 只切割一次 取最后一个字符串
            file = order.split(' ')[-1]
            download_file(sock,file)
        elif order[:3] == "PUT":
            file = order.split(' ')[-1]
            put_file(sock, file)
        else:
            print("输入命令有误，重新输入")
        # sock.send(msg.encode())
        # data = sock.recv(1024)
        # print("客户端收到的消息为：",data.decode())
    sock.close()


def get_file_list(sock):
    sock.send("LIST".encode())
    data = sock.recv(1024).decode()
    if data == "OK":
        while True:
            file_name = sock.recv(1024).decode()
            # 接收服务端的退出标识 跟UDP 不同 读到最后不会返回空
            if file_name == "##":
                break
            print(file_name)

    else:
        print("读取文件出错了")


if __name__ == '__main__':
    main()
