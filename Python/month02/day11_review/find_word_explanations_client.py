"""
    UDP查询单词的客户端
"""
import socket
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)
while True:
    word = input('>>>>>')
    udp_socket.sendto(word.encode(), ('127.0.0.1', 34567))
    if not word:
        break
    mean,address = udp_socket.recvfrom(1024)
    print(mean.decode())
udp_socket.close()