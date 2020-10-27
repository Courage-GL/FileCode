"""
web server 程序

完成一个类，提供给使用者
可以通过这个类快速搭建服务
完成网页展示
"""
from socket import *
from select import *
import os


class WebServer:
    def __init__(self, host="0.0.0.0", port=80, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.rlist = []
        self.wrist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        # HTTP协议 内部只能使用TCP协议
        self.sock = socket()
        self.sock.setblocking(False)
        self.rlist.append(self.sock)

    # 绑定IP地址
    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    def handle(self,connfd, data):
        data_list = data.split(" ")
        info = data_list[1]
        if info == "/":
            filename = self.html + "/index.html"
        else:
            filename = self.html + info
        # 打开判断文件是否存在
        try:
            file = open(filename, "rb")
        except:
            # 　请求的网页不存在
            response = "HTTP/1.1 404 Not Found\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            with open(self.html + "/404.html") as file:
                response += file.read()
            response = response.encode()
        else:
            # 请求的网页存在
            data = file.read()  # 字节串
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n" % len(data)
            response += "\r\n"
            response = response.encode() + data
            file.close()
        finally:
            connfd.send(response)


    # 启动整个服务
    def start(self):
        self.sock.listen(5)
        while True:
            rlist, wlist, xlist = select(self.rlist, self.wrist, self.xlist)
            for r in rlist:
                if r is self.sock:
                    conndf, addr = self.sock.accept()
                    conndf.setblocking(False)
                    self.rlist.append(conndf)
                else:
                    data = r.recv(1024)
                    if not data:
                        self.rlist.remove(r)
                        r.close()
                        continue
                    self.handle(r,data.decode())


if __name__ == '__main__':
    # 需要用户决定:地址 网页
    httpd = WebServer(host="0.0.0.0",
                      port=12345,
                      html="../static")
    # 启动服务
    httpd.start()
