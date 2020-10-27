import socket
ADDRESS = ('127.0.0.1',33337)
xiaomei_socket = socket.socket()
xiaomei_socket.connect(ADDRESS)
while True:
    word = input('>>').encode()
    if not word:
        break
    xiaomei_socket.send(word)
    data = xiaomei_socket.recv(1024)
    print(data.decode())
xiaomei_socket.close()

