"""
    WEB_SERVER
    需求分析
    技术点: HTTP协议
           IO多路复用的并发网络模型
    功能划分和封装:类封装
    协议:Http协议
    逻辑实现步骤:

"""


from socket import *
from select import *
class Web_Server:
    def __init__(self):
        pass
    def main(self):
        p = poll()
        s = socket()
        s.bind(("0.0.0.0", 1234))
        s.listen(5)
        p.register(s, POLLIN)
        map[s.fileno()] = s
        while True:
            events = p.poll()
            # fd 文件描述符 event是准备就绪的事件类型 真正的事件对象在map里存放着
            for fd, event in events:
                # 有客户端连接
                if fd == s.fileno():
                    connfd, addr = map[fd].accept()
                    print("CONNECT FROM ", addr)
                    # 设置为非阻塞状态
                    connfd.setblocking(False)
                    # 将连接套接字也放到rlist里面
                    p.register(connfd, POLLIN | POLLERR)
                    map[connfd.fileno()] = connfd
                elif event == POLLIN:
                    # 客户端发消息 connfd就绪
                    data = map[fd].recv(1024)
                    # 客户端退出的处理
                    if not data:
                        p.unregister(fd)
                        map[fd].close()
                        del map[fd]
                        continue
                        # 接收浏览器发送的请求
                    result = data.decode()
                    result_list = result.split(" ")
                    # 分情况讨论
                    if result_list[1] == "/python":
                        response = "HTTP/1.1 200 ok\r\n"
                        response += "Content-Type: text/html\r\n"
                        response += "\r\n"
                        with open("../python.html", "r") as f:
                            for line in f:
                                response += line
                    else:
                        # 发送http响应给浏览器
                        response = "HTTP/1.1 404 not fuobd\r\n"
                        response += "Content-Type: text/html\r\n"
                        response += "\r\n"
                        response += "SORRY...."
                    map[fd].send(response.encode())





