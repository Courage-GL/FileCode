"""
    webserver
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
        self.wlist = []
        self.xlist = []
        self.create_socket()
        self.bind()

    # 创建套接字
    def create_socket(self):
        # HTTP协议 内部只能使用TCP协议
        self.sock = socket()
        self.sock.setblocking(False)

    # 绑定IP地址
    def bind(self):
        self.address = (self.host, self.port)
        self.sock.bind(self.address)

    # 启动整个服务
    def start(self):
        self.sock.listen(5)
        self.rlist.append(self.sock)
        print("Listen the port %d" % self.port)
        while True:
            # 到这里阻塞监控
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sock:
                    tcpconfd, addr = self.sock.accept()
                    tcpconfd.setblocking(False)
                    self.rlist.append(tcpconfd)
                else:
                    if not self.handle(r):
                        continue

    def handle(self, r):
        data = r.recv(1024).decode()
        result_list = data.split(" ")
        response = "HTTP/1.1 200 ok\r\n"
        response += "Content-Type: text/html\r\n"
        response += "\r\n"
        file_list = os.listdir(self.html)
        if not data:
            self.rlist.remove(r)
            r.close()
            return False
        elif result_list[1] == "/":
            with open(self.html+"/index.html", "r") as f:
                for line in f:
                    response += line
        elif result_list[1].replace("/", "") in file_list:
            path = self.html + result_list[1]
            with open(path, "r") as f:
                for line in f:
                    response += line
        else:
            path = self.html + "/404.html"
            with open(path, "r") as f:
                for line in f:
                    response += line
        r.send(response.encode())
        self.rlist.remove(r)
        r.close()


if __name__ == '__main__':
    # 需要用户决定:地址 网页
    httpd = WebServer(host="0.0.0.0",
                      port=1234,
                      html="../static")
    # 启动服务
    httpd.start()
