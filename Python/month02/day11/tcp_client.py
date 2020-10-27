"""
    TCP客户端
"""
import socket

ADDRESS = ('127.0.0.1', 8888)
tcp_client = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)
# 连接服务器
tcp_client.connect(ADDRESS)
while True:
    msg = input('---->')
    tcp_client.send(msg.encode())
    # if msg == '##':
    #     tcp_client.close()
    #     break
    if not msg:
        tcp_client.close()
        break
    data = tcp_client.recv(1024)
    print('RECEIVE_MSG--->', data.decode())

