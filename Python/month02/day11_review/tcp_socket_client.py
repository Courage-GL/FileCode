"""
    TCP客户端
"""
import socket
Address = ('127.0.0.1', 34569)
file = open('dog.jpeg', 'rb')
tcp_socket = socket.socket(socket.AF_INET,
              socket.SOCK_STREAM)

tcp_socket.connect(Address)
for line in file:
    if not line:
        break
    tcp_socket.send(line)
tcp_socket.close()