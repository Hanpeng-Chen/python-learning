# 定义一个简单的函数
def print_str():
    print('hello world!')

print_str()

# 定义一个带参数的函数
def print_string(str):
    print(str)

print_string('Hello World!!!!')


# 返回多个值
def test(x, y):
    x1 = x + 2
    y1 = y + 3
    return x1, y1

x, y = test(10, 20)
print(x, y)


# 必备参数
# def print_necessary_params(str1):
#     print(str1)

# print_necessary_params()


# 关键字参数
def print_keyword_params(id, price):
    print('id:', id)
    print('price', price)

print_keyword_params(price=20, id=125345)

# 默认参数
def print_default_param(price = 50):
    print(price)

print_default_param()
print_default_param(20)


# 不定长参数
def print_info(arg1, *params):
    print('arg1:', arg1)
    for var in params:
        print(var)

print_info('test')
print_info(10, 20, 30, 40)


# 递归函数
def fact(n):
    """
    计算阶乘
    """
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))
print(fact(10))