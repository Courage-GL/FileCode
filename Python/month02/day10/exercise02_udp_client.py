import socket

udp_socket= socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)

while True:
    word = input("请输入单词：")
    if not word:
        udp_socket.close()
        break
    udp_socket.sendto(word.encode(),('127.0.0.1',34567))
    mean,address=udp_socket.recvfrom(1024)
    print(word,"的解释为",mean.decode())
