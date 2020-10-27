import socket
# 创建socket对象
address=('127.0.0.1', 45678)
db_socket = socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)
while True:
    word = input(">>")
    if not word:
        db_socket.close()
        break
    n=db_socket.sendto(word.encode(),address)
    mean,address = db_socket.recvfrom(1024)
    print("%s：%s" %(word,mean.decode()))


