"""
    练习：创建一个数据库 dict
        创建一个数据表 words
        id word mean
"""
import pymysql
word_list=[]
file = open("dict.txt") # 读打开
# 查找单词
for line in file:
    # 提取单词和解释
    tmp = line.split(' ',1)
    word_list.append(tuple(tmp))

file.close()


db = pymysql.connect(host='192.168.196.128',
                     port=3306,
                     user='root',
                     password='123456',
                     database='dict',
                     charset='utf8')
cur = db.cursor()
# sql1 = "delete from word where mean is not null"
sql = "insert into words(word,mean) values (%s,%s)"

try:
    # cur.execute(sql1)
    # # 方式一
    # for row in word_list:
    #     print(row)
    #     cur.execute(sql,row)
    # # 方式二
    cur.executemany(sql, word_list)
    cur.execute("select * from word")
    print(cur.fetchall())
    db.commit()
except Exception as e:
    print(e)

    db.rollback()
cur.close()
db.close()


