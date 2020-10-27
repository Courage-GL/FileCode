"""
    TCP服务端
"""
import socket
import os
from time import sleep

HOST = "127.0.0.1"
PORT = 4556
ADDRESS = (HOST, PORT)
FTP = "../work/"


def get_file_list(tcponf):
    print(os.listdir(FTP))
    if os.listdir(FTP):
        tcponf.send("OK".encode())
        sleep(0.1)
        # 一次发送所有文件名
        data = "\n".join(os.listdir(FTP))
        tcponf.send(data.encode())
        # 为了防止粘包 隔一段时间再发
        sleep(0.1)
        # 给客户端发送退出接收消息的标识
        tcponf.send(b"##")
    else:
        tcponf.send("FAIL".encode())


def download_file(tcp, file):
    try:
        print(FTP + file)
        old_file = open(FTP + file, 'rb')
    except:
        tcp.send("FAIL".encode())
        return
    else:
        tcp.send("OK".encode())
        sleep(0.1)
        while True:
            data = old_file.read(1024)
            if not data:
                break
            tcp.send(data)
        sleep(0.1)
        tcp.send("##".encode())


def put_file(connfd, filename):
    # 判断文件是否已存在
    if os.path.exists(FTP + filename):
        connfd.send(b"FAIL")
        return
    else:
        connfd.send(b"OK")
        # 接收文件
        f = open(FTP + filename, 'wb')
        while True:
            data = connfd.recv(1024)
            if data == b"##":
                break
            f.write(data)
        f.close()


def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)

    sock.bind(ADDRESS)
    sock.listen(5)
    while True:
        try:
            tcponf, addr = sock.accept()
        except KeyboardInterrupt:
            break
        while True:
            data = tcponf.recv(1024).decode()
            if not data or data == "EXIT":
                break
            elif data == "LIST":
                get_file_list(tcponf)
            elif data[:3] == "GET":
                file = data.split(" ")[-1]
                download_file(tcponf, file)
            elif data[:3] == "PUT":
                file = data.split(" ")[-1]
                put_file(tcponf, file)
            # print("服务端收到的内容为:",data.decode())
            # tcponf.send("服务端收到数据了".encode())

        tcponf.close()
    sock.close()


if __name__ == '__main__':
    main()
