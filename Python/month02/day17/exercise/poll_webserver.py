from select import *
from socket import socket


class PollWebServer:
    def __init__(self, host="0.0.0.0", port=12345, html=None):
        self.host = host
        self.port = port
        self.html = html
        self.response=""
        self.events_map = {}
        self.create_socket()

    def handle(self, connfd, data,p):
        data_list = data.split(" ")
        result = data_list[1]
        if result == "/":
            file_name = self.html + "/index.html"
        else:
            file_name = self.html + result
        try:
            file = open(file_name, "rb")
        except:
            file = open(self.html + "/404.html", "rb")
            response = "HTTP/1.1 404 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "\r\n"
            response = response.encode() + file.read()
            file.close()
        else:
            flie_data = file.read()
            response = "HTTP/1.1 200 OK\r\n"
            response += "Content-Type:text/html\r\n"
            response += "Content-Length:%d\r\n" % len(flie_data)
            response += "\r\n"
            response = response.encode() + flie_data
            file.close()

        finally:
            # self.response = response
            # p.register(connfd,POLLOUT)
            # self.events_map[connfd.fileno] = connfd
            connfd.send(response)

    def start(self):
        self.sock.listen(5)
        p = poll()
        self.sock.setblocking(False)
        self.events_map[self.sock.fileno()] = self.sock
        p.register(self.sock, POLLIN)
        while True:
            events = p.poll()
            for fileno, event in events:
                if fileno == self.sock.fileno():
                    connfd, addr = self.events_map[fileno].accept()
                    p.register(connfd, POLLIN)
                    self.events_map[connfd.fileno()] = connfd
                elif event == POLLIN:
                    data = self.events_map[fileno].recv(1024)
                    print(data.decode())
                    if not data:
                        p.unregister(self.events_map[fileno])
                        self.events_map[fileno].close()
                        del self.events_map[fileno]
                        continue
                    self.handle(self.events_map[fileno], data.decode(),p)
                elif event == POLLOUT:
                    pass
                    # self.events_map[fileno].send(self.response)
                    # # p.unregister(self.events_map[fileno])
                    # p.register(self.events_map[fileno], POLLIN)

    # 创建socket对象
    def create_socket(self):
        self.address = (self.host, self.port)
        self.sock = socket()
        self.sock.bind(self.address)


poll_webserver = PollWebServer(host="0.0.0.0",
                               port=12345,
                               html="../static")
poll_webserver.start()
