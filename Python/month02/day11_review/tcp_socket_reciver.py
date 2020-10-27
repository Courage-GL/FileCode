"""
    TCP_SOCKET 服务器端
"""
import socket
Address = ('127.0.0.1', 34569)
file = open('a.png','wb')
tcp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)

tcp_socket.bind(Address)
tcp_socket.listen(5)
connfig, address = tcp_socket.accept()
while True:
    print('<---WAITING FOR CONNECTION--->')
    data = connfig.recv(1024)
    if not data:
        break
    print('<---RECEIVED MSG--->')
    file.write(data)
tcp_socket.close()