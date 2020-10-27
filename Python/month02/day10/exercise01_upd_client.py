import socket

udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)


while True:
    msg = input(">>")
    # 当没有消息的时候 退出循环
    if not msg:
        udp_socket.close()
        break
    n = udp_socket.sendto(msg.encode(), ('127.0.0.1', 34567))
    print('发送了%d个字节' % n)
    data, address = udp_socket.recvfrom(1024)
    print(data.decode(), address)
