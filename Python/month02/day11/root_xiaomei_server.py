import socket

answer = {}
ADDRESS = ('0.0.0.0', 33337)


def get_answer():
    file = open('chat.txt', 'r')
    for line in file:
        word = line.split(' ', 1)
        answer[word[0]] = word[1]
    file.close()


def find_answer():
    xiaomei_socket = socket.socket()
    xiaomei_socket.bind(ADDRESS)
    xiaomei_socket.listen(5)
    udpsocket, address = xiaomei_socket.accept()
    while True:
        data = udpsocket.recv(1024).decode()
        if not data:
            break
        for key, value in answer.items():
            if key in data:
                udpsocket.send(value.encode())
                break
        else:
            udpsocket.send('我还小，不知道啦'.encode())

    udpsocket.close()


def main():
    get_answer()
    find_answer()


if __name__ == '__main__':
    main()
