"""
    作业： 1. 进程函数使用熟练，自定义进程类

      2. 求100000以内质数之和，写成一个函数
         写一个装饰器求一个这个函数运行时间

         将100000分成4等份 分别使用4个进程求
         每一份的质数之和，四个进程同时执行
         记录时间

         将100000分成10等份 分别使用10个进程求
         每一份的质数之和，10个进程同时执行
         记录时间
"""
import time

class MyNumber:
    # pass
    # 结果为----> 454396537
    # 耗时为----> 27.815834283828735
    # 结果为 - ---> 454396537
    # 耗时为 - ---> 13.165640115737915
    def sum_pri_num_by100000(self):
        """
        100000以内质数求和
        :return: 求和结果
        """
        start_time = time.time()
        result = 0
        for num in range(2, 100001):
            for i in range(2, num//2+1):
                if num % i == 0:
                    # print(num)
                    break
            else:
                result += num
        end_time = time.time()
        print("结果为---->", result)
        print("耗时为---->", end_time-start_time)


my_number = MyNumber()
my_number.sum_pri_num_by100000()
