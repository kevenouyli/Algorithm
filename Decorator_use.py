##1、自定义装饰器，强化单体模型的类。
instances = {} # 全局变量，管理实例
def getInstance(aClass, *args):
    if aClass not in instances:
        instances[aClass] = aClass(*args)
    return instances[aClass]     #每一个类只能存在一个实例

def singleton(aClass):
    def onCall(*args):
        return getInstance(aClass,*args)
    return onCall
######################## 使用nonlocal处理外部变量。
# def singleton(aClass):
# 	instance = None
# 	def onCall(*args):
# 		nonlocal instance
# 		if instance == None:
# 			instance = aClass(*args)
# 		return instance
# 	return onCall
############################  使用类处理外部变量。
# class singleton:
# 	def __init__(self,aClass):
# 		self.aClass = aClass
# 		self.instance = None
# 	def __call__(self,*args):
# 		if self.instance == None:
# 			self.instance = self.aClass(*args)
# 		return self.instance
############################

@singleton  # Person = singleton(Person)
class Person:
    def __init__(self, name, hours, rate):
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton  # Spam = singleton(Spam)
class Spam:
    def __init__(self, val):
        self.attr = val


bob = Person('Bob', 40, 10)
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)
print(sue.name, sue.pay())

X = Spam(42)
Y = Spam(99)
print(X.attr, Y.attr)