"""
    udp服务器端 基础功能代码示例
    重点代码！！！
"""
import socket
# 创建套接字
udp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_DGRAM)
# 绑定ip地址
udp_socket.bind(('0.0.0.0',34567))
# 接收消息
data, addr=udp_socket.recvfrom(1024)
print(data.decode(),addr)
n=udp_socket.sendto(b'Thank you',addr)
print("发送了%d个字节串" %n)
udp_socket.close()
