import socket

HOST = '0.0.0.0'
PORT = 3306
ADDR = (HOST, PORT)
# 储存用户信息的字典
user = {}


def login(my_socket, name, addr):
    if name in user:
        my_socket.sendto('FAIL'.encode(), addr)
    else:
        my_socket.sendto('OK'.encode(), addr)
        msg = '欢迎%s进入聊天室' % name
        for i in user:
            # 循环通知其他人
            my_socket.sendto(msg.encode(), user[i])
        # 增加该用户
        user[name] = addr


def chat(my_socket, chat, addr):
    chat_list = chat.split(" ")
    if chat_list[0] in user:

        msg = "%s:%s" % (chat_list[0], chat_list[1])
        for i in user:
            if i == chat_list[0]:
                continue
            # 循环通知其他人
            my_socket.sendto(msg.encode(), user[i])
    else:
        my_socket.sendto('FAIL'.encode(), addr)


if __name__ == '__main__':
    my_socket = socket.socket(socket.AF_INET,
                              socket.SOCK_DGRAM)
    my_socket.bind(ADDR)
    while True:
        data, addr = my_socket.recvfrom(1024)
        recv_msg = data.decode()
        try:
            recv_msg_list = recv_msg.split(" ", 1)
            if recv_msg_list[0] == "LOGIN":
                login(my_socket, recv_msg_list[1], addr)
            elif recv_msg_list[0] == "CHAT":
                chat(my_socket, recv_msg_list[1], addr)
            elif recv_msg_list[0] == "EXIT":
                print("%s退出了聊天室。" % recv_msg_list[1])
        except:
            my_socket.sendto('FAIL'.encode(), addr)
