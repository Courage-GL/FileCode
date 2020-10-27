"""
    SELECT IO 多路复用
"""
import socket
from select import select

file = open("log.txt", "a+")

sock_tcp = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
sock_tcp.bind(("0.0.0.0", 12345))
sock_tcp.listen(5)


sock_udp = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)

print("开始监控IO")
# 当IO发生的时候 就会打印相对应得IO列表
rs, ws, xs = select([file,sock_tcp,sock_udp], [file,sock_udp,sock_tcp], [sock_tcp,sock_udp,file])
print("rs", rs)
print("ws", ws)
print("xs", xs)
