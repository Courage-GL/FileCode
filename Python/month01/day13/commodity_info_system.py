"""
    创建commodity_info_system.py文件
    创建商品信息管理系统
        Model       -> 封装数据
        View        -> 界面逻辑
        Controller  -> 业务逻辑
"""
# 参照day10/exercise03
class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price
