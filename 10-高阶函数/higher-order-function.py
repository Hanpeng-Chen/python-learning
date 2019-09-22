# 参数为函数
def print_hello():
    print('hello world')

def print_function(func):
    func()
    print('in the print_function')

print_function(print_hello)


# 返回值为函数
def print_hello():
    print('hello world')

def print_function():
    print('in the print_func')
    return print_hello

result = print_function()
result()