"""
    图片拷贝 客户端
"""
import socket
file = open('dog.jpeg','rb')
upd_socket = socket.socket(socket.AF_INET,
              socket.SOCK_DGRAM)
for item in file:
    upd_socket.sendto(item, ('127.0.0.1', 34567))
    if not item:
        break
    print(item)
upd_socket.sendto(b'##', ('127.0.0.1', 34567))
print("拷贝完成")





