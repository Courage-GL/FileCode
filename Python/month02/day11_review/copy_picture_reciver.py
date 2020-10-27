"""
    udp实现图片拷贝服务端
"""
import socket
Address = ('0.0.0.0',34567)
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)

udp_socket.bind(Address)
file = open('my_picture.png', 'wb')

while True:
    data, address = udp_socket.recvfrom(1024)
    if data == b'##':
        break
    file.write(data)
    print(data)
file.close()
udp_socket.close()




