import re

phone = '010-23123453 # 这是一个电话号码'

# 删除注释
num = re.sub(r'#.*$', '', phone)
print(num)

num1 = re.sub(r'\D', '', phone)
print(num1)