"""
    UDP查询单词的服务端
    192.168.196.128
"""
import socket
import pymysql

Address = ('0.0.0.0', 34567)


def find_mean(word):
    sql = "select mean from words where word=%s"
    cur.execute(sql, [word])
    mean = cur.fetchone()
    if not mean:
        return '数据库里没有该单词'
    return mean[0]


def get_word():
    udp_socket = socket.socket(socket.AF_INET,
                               socket.SOCK_DGRAM)
    udp_socket.bind(Address)
    while True:
        word, address = udp_socket.recvfrom(1024)
        if not word:
            break
        mean = find_mean(word.decode())
        udp_socket.sendto(mean.encode(), address)
    udp_socket.close()


if __name__ == '__main__':
    db = pymysql.connect(host='192.168.196.128',
                         port=3306,
                         user='root',
                         password='123456',
                         database='dict',
                         charset='utf8')
    cur = db.cursor()
    get_word()
