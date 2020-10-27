import socket
import pymysql

udp_socket = socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)
udp_socket.bind(('0.0.0.0',34567))
db = pymysql.connect(host='192.168.196.128',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
while True:
    word, address = udp_socket.recvfrom(1024)

    if not word:
        udp_socket.sendto("输入的单词不能为空".encode(),address)
        break
    try:
        cur.execute("select mean from words where word='%s'" % word.decode())
        result = cur.fetchone()[0].strip()
        udp_socket.sendto(result.encode(), address)
        # db.commit()
    except Exception as e:
        print(e)
        db.rollback()
        cur.close()
        db.close()


