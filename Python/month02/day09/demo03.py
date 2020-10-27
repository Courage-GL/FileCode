"""
executemany 多次执行SQL命令，执行次数由列表中元组数量决定
参数： sql sql语句
      list_  列表中包含元组 每个元组用于给sql语句传递参量，一般用于写操作
"""
import pymysql
l = [("Dave", 16, 'm', 81),
         ("Levi", 17, 'w', 86),
         ("Ala", 19, 'w', 85),
         ("Han", 21, 'm', 88)]
db = pymysql.connect(host='192.168.196.128',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()
sql = "insert into student1(name,age,sex,score) values (%s,%s,%s,%s)"

try:
    # 方式一
    # for row in l:
    #     cur.execute(sql)
    # 方式二
    cur.executemany(sql, l)
    cur.execute("select * from student1")
    print(cur.fetchall())
    db.commit()
except:
    db.rollback()
cur.close()
db.close()
