import socket
ADDR = ("127.0.0.1",12345)
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_STREAM)
sock.connect(ADDR)

while True:
    msg = input("---->")
    if not msg:
        break
    sock.send(msg.encode())
    data =sock.recv(1024)
    print(data.decode())

