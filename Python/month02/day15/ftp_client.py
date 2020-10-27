"""
    FTP文件传输客户端
"""

import socket
from multiprocessing import Process
import os

FTP = "WORK1/"


def show_selects():
    print("1.查看所有文件")
    print("2.下载文件")
    print("3.上传文件文件")
    print("4.退出")


def see_all_file(tcp_client):
    tcp_client.send("LIST".encode())


def down_file(tcp_client):
    tcp_client.send("DOWNLOAD".encode())


def upload_file(tcp_client):
    tcp_client.send("UPLOAD".encode())
    files = os.listdir(FTP)
    if not files:
        tcp_client.send("FTP列表里没有文件\n".encode())
    else:
        # 用\n来拼接flies
        tcp_client.send("UPLOAD:\n".encode())
        data = "\n".join(files)
        tcp_client.send(data.encode())


def exit_system(tcp_client):
    print("退出系统,谢谢使用")
    tcp_client.send("EXIT".encode())


def get_msg_from_server(tcp_client):
    while True:
        data = tcp_client.recv(1024).decode()
        if data == "EXIT":
            break

        # print()
        datalist = data.split("\n")
        if datalist[0] == "COPY:":
            datalist.remove("COPY:")
            print('\n%s\n文件即将开始拷贝' % datalist)
            if not os.path.exists(FTP):
                os.mkdir(FTP)
            for file in datalist:
                with open("work/" + file, "rb") as old_file:
                    with open(FTP + file, "wb") as new_file:
                        for line in old_file:
                            new_file.write(line)
            print("文件拷贝完成")
            print('\n请输入您的选择:')

        elif datalist[0] == "FILE:":
            datalist.remove("FILE:")
            print('\n%s\n请输入您的选择:' % datalist)

    tcp_client.close()


def main():
    ADDRESS = ('127.0.0.1', 12345)
    tcp_client = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM)
    # 连接服务器
    tcp_client.connect(ADDRESS)
    p = Process(target=get_msg_from_server, args=(tcp_client,))
    p.daemon = True
    p.start()
    while True:
        show_selects()
        try:
            select = input("请输入您的选择：")
            if not select:
                print("什么也没输入，客户端退出。")
                tcp_client.send("EXIT".encode())
                break
            if select in ("1", "2", "3", "4"):
                if select == "1":
                    see_all_file(tcp_client)
                elif select == "2":
                    down_file(tcp_client)
                elif select == "3":
                    upload_file(tcp_client)
                else:
                    exit_system(tcp_client)
                    break
                # break
            else:
                print("您的输入有误请重新输入：")
        except KeyboardInterrupt:
            print("强制退出系统，系统结束")
            break


if __name__ == '__main__':
    main()
