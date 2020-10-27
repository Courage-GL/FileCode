"""
练习： input输入一个学生的姓名 ，将该学生的成绩改为100分
"""
import pymysql

input_name = input("输入姓名：\n")
db = pymysql.connect(host='192.168.196.128',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
cur = db.cursor()
try:
    # 第一种方法
    # sql = "insert into student1(name) values('小红')"
    # sql1 = 'update student1 set score=100 where name="%s"' % input_name
    # cur.execute(sql1)
    # 第二种方法
    sql2 = 'update student1 set score=%s where name=%s'
    cur.execute(sql2, [16, input_name])
    cur.execute("select * from student1")
    print(cur.fetchall())
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
    print("出现问题，回滚")
cur.close()
db.close()
