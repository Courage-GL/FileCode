"""
    练习1：画出下列代码内存图，并写出打印结果。
    def func01(p1, p2):
        p1 = "孙悟空"
        p2["八戒"] += 50
    a = "悟空"
    b = {"八戒": 100}
    func01(a, b)
    print(a) # ?
    print(b) # ?
"""

def func01(p1, p2):
    p1 = "孙悟空"
    p2["八戒"] += 50


a = "悟空"
b = {"八戒": 100}
func01(a, b)
print(a)  # ?
print(b)  # ?