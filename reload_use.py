# Method 	    Overloads 	    Call for
# __init__ 	    构造函数 	         X=Class()
# __del__ 	    析构函数 	         对象销毁
# __repr__ 	    打印转换          print X，repr(X)
# __str__ 	    打印转换 	         print X，str(X)
# __call__  	调用函数 	         X()
# __getattr_ 	限制 	         X.undefine
# __setattr__ 	取值 	         X.any=value
# __getitem__ 	索引 	         X[key]，For If
# __setitem__ 	索引 	         X[key]=value
# __len__ 	    长度 	         len(X)
# __iter__ 	    迭代              For In
# __add__ 	    + 	             X+Y,X+=Y
# __sub__ 	    - 	             X-Y,X-=Y
# __mul__ 	    * 	              X*Y
# __radd__ 	    右加+ 	          +X
# __iadd__ 	    += 	             X+=Y
# __or__ 	    | 	             X|Y,X|=Y
# __cmp__ 	    比较 == 	         X==Y,X<Y
# __lt__ 	    小于< 	            X<Y
# __eq__ 	    等于= 	            X=Y

########################矩阵重载######################
print("矩阵重载：")
class Vector4:
    def __init__(self,a,b,c,d):
       (self.a1,self.a2,self.a3,self.a4)=(a,b,c,d)
    def __mul__(self,other):
         return (self.a1*other.a1+self.a2*other.a2+self.a3*other.a3+self.a4*other.a4)
    def PrintVector(self):
        print (self.a1,self.a2,self.a3,self.a4)
class Matrix :
    def __init__(self,a,b,c,d):
        (self.a1,self.a2,self.a3,self.a4)=(a,b,c,d)

    def __mul__(self, other):
        x1=Vector4(other.a1.a1, other.a2.a1, other.a3.a1, other.a4.a1)   # other(矩征）.a1（向量）.a1（数值）
        x2=Vector4(other.a1.a2, other.a2.a2, other.a3.a2, other.a4.a2)
        x3=Vector4(other.a1.a3, other.a2.a3, other.a3.a3, other.a4.a3)
        x4=Vector4(other.a1.a4, other.a2.a4, other.a3.a4, other.a4.a4)
        a=Vector4(self.a1*x1, self.a1*x2, self.a1*x3, self.a1*x4)
        b=Vector4(self.a2*x1, self.a2*x2, self.a2*x3, self.a2*x4)
        c=Vector4(self.a3*x1, self.a3*x2, self.a3*x3, self.a3*x4)
        d=Vector4(self.a4*x1, self.a4*x2, self.a4*x3, self.a4*x4)
        return Matrix(a, b, c, d)
    def PrintMatrix(self):
         self.a1.PrintVector()
         self.a2.PrintVector()
         self.a3.PrintVector()
         self.a4.PrintVector()
i1 = Vector4(1, 4, 1, 4)
i2 = Vector4(2, 1, 6, 7)
k=i1*i2
#测试向量点乘
print (k)
i3=Vector4(1,1,1,1)
i4=Vector4(1,2,4,5)
j1=Vector4(1,2,3,4)
j2=Vector4(2,1,1,1)
j3=Vector4(1,3,21,2)
j4=Vector4(2,4,3,7)
a=Matrix(i1,i2,i3,i4)
b=Matrix(j1,j2,j3,j4)
print("a:")
a.PrintMatrix()
print("b:")
b.PrintMatrix()
c=a*b
print("c:")
c.PrintMatrix()

########################索引重载######################
print("索引重载：")
class indexer_1:
    def __getitem__(self, index):  # iter override
        return index ** 2

X = indexer_1()
for i in range(5):
    print(X[i])

class indexer_2:
    def __init__(self):
        self.mydict={}
    def __setitem__(self, key, value):  # iter override
        self.mydict[key] = value
        return self.mydict

X2 = indexer_2()
X2[2] = 'test'
print (X2.mydict.items())


########################打印重载######################
print("打印重载：")
class adder :
    def __init__(self,value=0):
           self.data=value
    def __add__(self,other):
           self.data+=other
class addrepr(adder):
    def __repr__(self):
          return "addrepr(%d)"% self.data #%d ,%s都可以
x=addrepr(2)
x+1
print (x ,repr(x))  #对象描述符函数 repr()，等同于内置__repr__函数


########################调用重载######################      __call__相当与 X()
print("调用重载：")
class Prod:
    def __init__(self, value):
        self.value = value

    def __call__(self, other):
        return self.value * other


p = Prod(2)  # call __init__
print(p(1))  # call __call__
print(p(2))

########################析构重载######################     __del__
print("析构重载：")
class Life:
    def __init__(self, name='name'):
        print('Hello', name)
        self.name = name

    def __del__(self):
        print('Goodby', self.name)

brain = Life('Brain')  # call __init__
brain = 'loretta'  # call __del__


########################重载"|"######################
print("重载\"|\"：")
class Mat :
    def __init__(self,value):
       self.age=value
    def __or__(self,other):
        return self.age!=0 and other.age!=0
a=Mat(10)
b=Mat(21)
c=Mat(0)
print (a|b ,a|c)


########################长度重载######################
print("长度重载：")
class lenOperator:
    def __init__(self,*arg):
        self.arg=[]
        for e in arg:
            self.arg.append(e)
    def __len__(self):
        return len(self.arg)
a=lenOperator(0,2,4,7,8,9)
print (len(a))

########################cmp重载######################
print("cmp重载：")
class cmpOperator:
    def __init__(self,a,b,c):
        (self.a,self.b,self.c)=(a,b,c)
    def __cmp__(self,other):
        if self.a>other.a:
           return 1
        elif self.a<other.a:
           return -1
        elif self.b>other.b:
           return 1
        elif self.b<other.b:
            return -1
        elif self.c>self.c:
            return 1
        elif self.c<self.c:
            return -1
        elif self.c==self.c:
           return 0
i=cmpOperator(1,2,3)
j=cmpOperator(2,4,5)
k=cmpOperator(2,4,5)
a=cmpOperator(1,4,5)
print((i==j),(j.__cmp__(k)),(i.__cmp__(j)))

########################delattr重载######################
print("delattr重载：")
class delattrOperator(object):
    def __init__(self, a, b):
        (self.a, self.b) = (a, b)

    def __delattr__(self, name):
        print("del obj.%s" % name)
        object.__delattr__(self, name)

a = delattrOperator(1, 2)
print(a.a, a.b)
del a.a
print(a.b)
# print a.a 打印a会出错，a已经被删除。

########################getAttr/setAttr重载######################
print("getattr重载：")
class empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            print(attrname)

X = empty()
print(X.ages)       # call__getattr__


print("setattr重载：")
class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            # Self.attrname = value loops!
            self.__dict__[attr] = value
        else:
            print(attr + '  is not allowed')
X = accesscontrol()
X.age = 40  # call __setattr__
X.name = 'wang'  # raise exception
