import socket
import pymysql
address = ('0.0.0.0', 45678)
db_socket = socket.socket(socket.AF_INET,
                          socket.SOCK_DGRAM)

db = pymysql.connect(host='192.168.196.128',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()

db_socket.bind(address)
while True:
    word,addr = db_socket.recvfrom(1024)
    sql = 'select mean from words where word=%s'
    print("要查询的单词为",word.decode())
    cur.execute(sql,[word.decode()])
    result=cur.fetchone()
    if not result:
        result = 'NOT FOUND'
    else:
        result = result[0].strip()
    print("查询结果为：",result)
    db_socket.sendto(result.encode(),addr)

