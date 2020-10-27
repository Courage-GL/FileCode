"""
    读操作
"""
import pymysql
# 192.168.196.128 虚拟机地址
# 连接到数据库
db = pymysql.connect(host="192.168.196.128",
                     port=3306,
                     user="root",
                     password="123456",
                     database="stu",
                     charset="utf8")
# 创建游标cursor对象 操作数据库数据，获取操作结果的对象
cur = db.cursor()
# 数据操作
sql = "select name,age,sex from student1 where score > 80"
cur.execute(sql)
print(cur.fetchall())
# 关闭游标跟数据库
cur.close()
db.close()
