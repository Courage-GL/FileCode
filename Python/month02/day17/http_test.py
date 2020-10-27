"""
    http请求
"""
from socket import *

s = socket()
s.bind(("0.0.0.0", 12345))
s.listen(5)

c, addr = s.accept()
print("CONNECT FROM ", addr)
data = c.recv(1024)
print(data.decode())
# 发送http响应给浏览器
response = """HTTP/1.1 200 OK
Content-Type: text/html

Hello world
"""
c.send(response.encode())
c.close()
s.close()
