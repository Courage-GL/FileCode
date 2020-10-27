"""
    聊天室客户端
    1.login 登录
    2.chat 开始聊天
    3.exit 退出聊天
"""
import socket
from multiprocessing import Process

ADDR = ("127.0.0.1", 3333)


def login(sock, msg):
    while True:
        sock.sendto(msg.encode(), ADDR)
        recv_msg, address = sock.recvfrom(1024)
        if recv_msg.decode() == "OK":
            print("加入聊天室成功。")
            break
        else:
            print("名字存在了，请重新输入")


def chat(sock):
    while True:
        recv_msg, addr = sock.recvfrom(1024)
        # msg=recv_msg.decode()
        msg = "\n%s\n发言:" % recv_msg.decode()
        print(msg, end="")


def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    name = input("Name:")
    msg = "LOGIN " + name
    login(sock, msg)
    # chat()
    p = Process(target=chat, args=(sock,))
    p.start()
    while True:
        content = input("发言:")
        word_content = "CHAT " + name + "  " + content
        sock.sendto(word_content.encode(), ADDR)

    p.join()


if __name__ == '__main__':
    main()
