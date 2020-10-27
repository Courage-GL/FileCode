import socket

ADDR = ("0.0.0.0", 3333)
users = {}


def for_login(sock, name, addr):
    if name in users:
        msg = "%s已经存在，请重新输入" % name
        sock.sendto(msg.encode(), addr)
    else:
        msg = "欢迎%s" % name
        for i in users:
            if i != name:
                sock.sendto(msg.encode(), users[i])
        users[name] = addr
        sock.sendto("OK".encode(), addr)


def for_chat(sock, name, chat_content):
    msg = "%s:%s" % (name, chat_content)
    for i in users:
        sock.sendto(msg.encode(), users[i])


def for_exit(sock, name):
    pass


def main():
    sock = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
    sock.bind(ADDR)
    while True:
        recv_msg, addr = sock.recvfrom(1024)
        msg_list = recv_msg.decode().split(" ", 2)
        if msg_list[0] == "LOGIN":
            for_login(sock, msg_list[1], addr)
        elif msg_list[0] == "CHAT":
            for_chat(sock, msg_list[1], msg_list[2])
        elif msg_list[0] == "EXIT":
            for_exit(sock, msg_list[1])


if __name__ == '__main__':
    main()
