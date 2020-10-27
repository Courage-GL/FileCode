"""
    练习：编写一个程序 如果浏览器访问127.0.0.1:8888/python
    的时候可以访问到Python.html 其它的 404
"""

"""
    http请求
"""
from socket import *

s = socket()
s.bind(("0.0.0.0", 1234))
s.listen(5)

c, addr = s.accept()
print("CONNECT FROM ", addr)
data = c.recv(1024)
# 接收浏览器发送的请求
result = data.decode()
result_list = result.split(" ")
response = ""
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
c.send(response.encode())
c.close()
s.close()
