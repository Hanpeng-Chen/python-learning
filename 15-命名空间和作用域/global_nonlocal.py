num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    print(num) 
    num = 123
    print(num)
fun1()
print(num)


def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        print(num)
    inner()
    print(num)
outer()



a = 10
def test():
    a = a + 1
    print(a)
test()


a = 10
def test(a):
    a = a + 1
    print(a)
test(a)