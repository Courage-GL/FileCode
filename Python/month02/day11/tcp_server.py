"""
    tcp 服务端代码示例
"""
import socket

ADDRESS = ('0.0.0.0', 8888)
# 参数如果不写 也是TCP
tcp_socket = socket.socket(socket.AF_INET,
                           socket.SOCK_STREAM)
# 绑定地址
tcp_socket.bind(ADDRESS)
# 设置监听 为连接做准备
tcp_socket.listen(1024)
while True:
    print('<-----WAITING FOR CONNECTION----->')
    # 等待客户端连接
    connfd, address = tcp_socket.accept()
    # listen accept 三次握手
    print('CONNECTION TO---->', address)
    while True:
        # 收到消息
        data = connfd.recv(1024)
        print("RECEIVE_MSG---->", data.decode())
        connfd.send(b'FUCK YOU')
        # if data.decode() == '##':
        #     # 关闭套接字
        #     # 四次挥手
        #     connfd.close()
        #     tcp_socket.close()
        #     break

        if not data:
            # 关闭套接字
            # 四次挥手
            connfd.close()
            break

