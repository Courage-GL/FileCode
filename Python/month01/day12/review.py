"""
    封装设计思想
        中心思想：分而治之，变则疏之
        类：行为的不同
            class 类名1：
                def 方法名1(self):
                    ...

            class 类名2：
                def 方法名2(self):
                    ...
        对象：数据的不同
            对象名 = 类名(数据1,数据2)

        跨类调用
            方法1：直接创建对象
            语义：每次用方法1,都创建新对象
            class 类名1:
                def __init__(self,形参):
                    self.数据1 = 形参

                def 方法名1(self):
                    对象名 = 类名2(实参)
                    对象名.方法名2()

            class 类名2:
                def 方法名2(self):
                    ...

            方法2：在构造函数创建对象
            语义：每次用我自己的实例变量方法
            class 类名1:
                def __init__(self,形参):
                    self.数据1 = 形参
                    self.对象名 = 类名2(实参)

                def 方法名1(self):
                    self.对象名.方法名2()

            class 类名2:
                def 方法名2(self):
                    ...

            方法3：在构造函数创建对象
            语义：类名1与类名2在使用时建立的联系
            class 类名1:
                def 方法名1(self,形参):
                    形参.方法名2()

            class 类名2:
                def 方法名2(self):
                    ...

            对象1 = 类名1()
            对象2 = 类名2()
            对象1.方法名1(对象2)
"""
