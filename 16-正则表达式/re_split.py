import re
print(re.split('\W+', 'runoob, runoob, runoob.'))
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
 
print(re.split('a*', 'hello world'))   # 对于一个找不到匹配的字符串而言，split 不会对其作出分割