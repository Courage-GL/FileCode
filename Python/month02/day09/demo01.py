# 查询数据库 pymysql 数据库处理结构示例
import pymysql
# 192.168.196.128 虚拟机地址
# 连接到数据库
db = pymysql.connect(host="192.168.196.128", port=3306, user="root", password="123456",
                     database="stu", charset="utf8")
# 创建游标cursor对象 操作数据库数据，获取操作结果的对象
cur = db.cursor()
# 数据操作
cur.execute("update student1 set name='小明' where id = 1")
cur.execute("select * from student1")
print(cur.fetchall())
# 关闭游标跟数据库
cur.close()
db.close()


