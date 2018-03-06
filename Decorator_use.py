###################1、自定义装饰器，强化单体模型的类。#####################
print("自定义装饰器，强化单体模型的类:")
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

###################2、跟踪对象接口#####################
print("跟踪对象接口:")
class Wrapper:
    def __init__(self, obj):
        self.wrapped = obj

    def __getattr__(self, attrname):
        print('Trace:', attrname)
        return getattr(self.wrapped, attrname)

x = Wrapper([1, 2, 3])
x.append(4)
print(x.wrapped)
x = Wrapper({'a': 1, 'b': 2})
print(list(x.keys()))

###################3、拦截实例创建调用，这里的类装饰器允许我们跟踪整个对象接口#####################
print("拦截实例创建调用，这里的类装饰器允许我们跟踪整个对象接口:")
def Tracer(aClass):
    class Wrapper:
        def __init__(self,*args,**kargs):
            self.fetches = 0
            self.wrapped = aClass(*args,**kargs)
        def __getattr__(self,attrname):
            print('Trace:'+attrname)
            self.fetches += 1
            return getattr(self.wrapped,attrname)
    return Wrapper

@Tracer
class Spam:
    def display(self):
        print('Spam!'*8)

@Tracer
class Person:
    def __init__(self,name,hours,rate):
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

food = Spam()
food.display()
print([food.fetches])

bob = Person('Bob',40,50)
print(bob.name)
print(bob.pay())

print('')
sue = Person('Sue',rate=100,hours = 60)
print(sue.name)
print(sue.pay())

print(bob.name)
print(bob.pay())
print([bob.fetches,sue.fetches])      ##跟踪每个实例调用任何属性的次数。

###################4、@property的用法#####################
class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if value >= 0 and value <= 100:
            self.__score = value  # 还记得__score吗？前面加一个双下划线，表示private私有属性
        else:
            raise ValueError('score must between 0 ~ 100!')

s = Student()
s.score = 90
print(s.score)