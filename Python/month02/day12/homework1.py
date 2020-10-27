"""
       将100000分成4等份 分别使用4个进程求
        每一份的质数之和，四个进程同时执行
"""
import time
from multiprocessing import Process


class QuartileProcess(Process):

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        super().__init__()

    def sum_pri_num(self, value1, value2):
        """
        value1-value2范围内的质数求和
        :return: 求和结果
        """
        start_time = time.time()
        result = 0
        for num in range(value1, value2):
            for i in range(2, num//2+1):
                if num % i == 0:
                    # print(num)
                    break
            else:
                result += num
        end_time = time.time()
        print("结果为---->", result)
        print("耗时为---->", end_time - start_time)

    def run(self):
        self.sum_pri_num(self.value1, self.value2)


if __name__ == '__main__':
    result = 0
    last_result = 0
    close_qp = []
    # for i in range(4):
    # result = 100000 // 4 * (i + 1)
    for i in range(10):
        result = 100000 // 10 * (i + 1)
        qp = QuartileProcess(last_result, result)
        qp.start()
        close_qp.append(qp)
        last_result = result

    for qp_item in close_qp:
        qp_item.join()

    """
        结果为----> 5736397
        耗时为----> 0.9704854488372803
        结果为----> 15434795
        耗时为----> 2.534334897994995
        结果为----> 24504673
        耗时为----> 3.77935791015625
        结果为----> 33494802
        耗时为----> 4.8372979164123535
        结果为----> 41842642
        耗时为----> 5.7299559116363525
        结果为----> 50835430
        耗时为----> 6.457756996154785
        结果为----> 57041680
        耗时为----> 6.786465167999268
        结果为----> 67597790
        耗时为----> 7.319227933883667
        结果为----> 74439106
        耗时为----> 7.785121202468872
        结果为----> 83469223
        耗时为----> 8.303719282150269
    """
