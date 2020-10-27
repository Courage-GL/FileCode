# 练习：使用学生列表封装以下三个列表中数据
list_student_name = ["悟空", "八戒", "白骨精"]
list_student_age = [28, 25, 36]
list_student_sex = ["男", "男", "女"]


class Student:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex


list_result = []
for item in zip(list_student_name, list_student_age, list_student_sex):
    stu = Student(*item)
    list_result.append(stu)

list_result = [Student(*item)
               for item in zip(list_student_name, list_student_age, list_student_sex)
               ]

print(list_result)
