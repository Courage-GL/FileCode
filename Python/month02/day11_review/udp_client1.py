"""
    udp 客户端
"""
import socket

udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)

while True:
    msg = input('>>>>>>')
    udp_socket.sendto(msg.encode(), ('127.0.0.1', 34567))
    if not msg:
        break
    data,address= udp_socket.recvfrom(1024)
    print(data.decode())

udp_socket.close()