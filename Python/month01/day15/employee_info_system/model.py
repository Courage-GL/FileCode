class EmployeeModel:
    def __init__(self, eid=0, did=0, name="", money=0):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

    def __str__(self):
        return "%s的编号是%d,部门编号是%d,工资是%d"%(self.name, self.eid, self.did, self.money)