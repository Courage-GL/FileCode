"""
    套接字使用
"""
import socket

# 创建一个UDP套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)
"""
    1.如果绑定的是127.0.0.1 或者localhost 那么另外一端只能在同一个计算机上通过127.0.0.1访问。
    2.如果绑定的是自己的IP地址 那么另外一端可以在任何位置通过该主机IP地址访问（公网IP或者在同一个局域网内）。
    3.如果绑定的是0.0.0.0 那么另外一端可以在同一计算机上通过127.0.0.1访问，或者在任何位置通过IP地址访问。
    
"""
# 绑定本机网络地址 参数只有一个 是一个元组
udp_socket.bind(('0.0.0.0', 3456))

n=udp_socket.sendto(b'hello,hello',("127.0.0.1",3456))
data, addr=udp_socket.recvfrom(1024)

print(data,addr,n)
udp_socket.close()




