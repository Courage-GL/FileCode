"""
    UDPfuwu1
"""
import socket
ADDRESS = ('0.0.0.0',34567)
# 创建udp套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)
udp_socket.bind(ADDRESS)
while True:
    data ,address = udp_socket.recvfrom(1024)
    if not data:
        break
    print('<-----RECEIVE_MAG----->')
    print(data.decode())
    udp_socket.sendto('我收到消息了，好开心啊'.encode(),address)

udp_socket.close()