class Employee:
    def __init__(self, name):
        self.name = name
    def __del__(self):
        print('destructor started')
    def skill(self):
        pass
class Cigna(Employee):
    def skill(self):
        print (self.name,'python')
class Walmart(Employee):
    def __skill(self):
        print (self.name,'java')

a = Employee('Raj')
a.testattr = 20
print(a.testattr)
a.skill()
a.testattr1 = 21
print(a.testattr1)
del a
    




