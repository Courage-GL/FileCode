"""
    基于select的 IO网络并发模型
    IO 多路复用与非阻塞搭配
    重点代码！！！
"""
from socket import *
from select import *

HOST = "0.0.0.0"
PORT = 12345
ADDR = (HOST,PORT)
sock = socket()
sock.bind(ADDR)
sock.listen(5)
# 设置非阻塞
sock.setblocking(False)
# 初始只有监听套接字
rlist = []
wlist = []
xlist = []
rlist.append(sock)

# 循环监控IO对象
while True:
    # 到这里阻塞监控
    rs, ws, xs = select(rlist, wlist, xlist)
    for r in rs:
        # 有客户端连接
        if r is sock:
            connfd, addr = r.accept()
            #设置为非阻塞状态
            connfd.setblocking(False)
            # 将连接套接字也放到rlist里面
            rlist.append(connfd)
            print(rlist)
        else:
            # 客户端发消息 connfd就绪
            data = r.recv(1024).decode()
            # 客户端退出的处理
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print("客户端传过来"+data)
            # r.send("OK".encode())
            # 存到写列表里
            wlist.append(r)

    for w in ws:
        w.send("OK".encode())
        # 写完要移除 要不会一直写
        wlist.remove(w)


