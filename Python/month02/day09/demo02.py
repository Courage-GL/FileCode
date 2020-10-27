import pymysql

"""
读操作
1.不支持事务的引擎 execute 会直接执行语句生效
2.不支持事务的引擎 写操作会默认开始一个事务
"""
db = pymysql.connect(host='192.168.196.128',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()
try:
    sql = "insert into student1(name) values('小红')"
    sql1 = 'update student1 set age=19 where id=8'
    cur.execute(sql1)
    cur.execute("select * from student1")
    print(cur.fetchall())
    db.commit()
except:
    db.rollback()
cur.close()
db.close()
