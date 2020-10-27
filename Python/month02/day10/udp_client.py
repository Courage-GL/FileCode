"""
    udp客户端
"""

import socket
# 创建套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)
msg = input(">>")
n=udp_socket.sendto(msg.encode(),('127.0.0.1',34567))
print('发送了%s个字节' %n)
# 接收消息
data, addr=udp_socket.recvfrom(1024)
print(data.decode(),addr)
udp_socket.close()