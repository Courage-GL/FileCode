import socket
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)
# 绑定ip地址
udp_socket.bind(('0.0.0.0',34567))
while True:
    data, address = udp_socket.recvfrom(1024)
    print("服务端收到了数据",data, address)
    n=udp_socket.sendto("收到了收到了".encode(),address)
    print('服务单发送了%d个字节' % n)

