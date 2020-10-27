"""
    SELECT IO 多路复用
"""
import socket
from select import *
map = {}
file = open("log.txt", "a+")

sock_tcp = socket.socket(socket.AF_INET,
                         socket.SOCK_STREAM)
sock_tcp.bind(("0.0.0.0", 12345))
sock_tcp.listen(5)


sock_udp = socket.socket(socket.AF_INET,
                         socket.SOCK_DGRAM)
# 查找字典 需要跟register的io保持一致

# 做准备
p = poll() #生成poll对象
p.register(sock_tcp,POLLIN|POLLERR)
p.register(sock_udp,POLLOUT|POLLERR)
p.register(file,POLLOUT|POLLERR)
map[sock_tcp.fileno()] = sock_tcp
map[sock_udp.fileno()] = sock_udp
map[file.fileno()] = file

print("开始监控IO")
events = p.poll()
for event in events:
    if event[0] in map:
        print(map[event[0]])

