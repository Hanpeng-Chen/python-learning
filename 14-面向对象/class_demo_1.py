class MyClass:
    i = 123
    def f(self):
        return 'hello world'

# 实例化类
x = MyClass()

# 访问类的属性和方法
print("MyClass类的属性 i 为：", x.i)
print("MyClass类的方法 f 输出：", x.f())

# __init__()方法
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(1, -1)
print(x.r, x.i)


# self
class Test:
    def prt(self):
        print(self)
        print(self.__class__)
 
t = Test()
t.prt()


class Test:
    def prt(runoob):
        print(runoob)
        print(runoob.__class__)
 
t = Test()
t.prt()