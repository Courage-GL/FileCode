"""
    二进制文件存储
"""

import pymysql

db = pymysql.connect(host='192.168.196.128',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()
try:
    # 写入
    # with open('a.jpeg', 'rb') as f:
    #     data = f.read()
    # sql = 'update student1 set image=%s where id=1'
    # cur.execute(sql,[data])
    # 读出
    cur.execute("select image from student1 where id=1")
    data=cur.fetchone()
    with open('dog.jpeg', 'wb') as f:
        f.write(data[0])
    db.commit()
except:
    db.rollback()
cur.close()
db.close()
