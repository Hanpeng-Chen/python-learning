class MyInputError(Exception):
    """Exception raised when there're errors in input"""
    def __init__(self, value): # 自定义异常类的初始化
        self.value = value
    def __str__(self): # 自定义异常类的String表达形式
        return ("{} is invalid input".format(repr(self.value)))

try:
    raise MyInputError(1)
except MyInputError as error:
    print('error: {}'.format(error))