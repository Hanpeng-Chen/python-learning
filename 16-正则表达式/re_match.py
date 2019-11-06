import re
print(re.match('www', 'www.chenhanpeng.com').span())  # 在起始位置匹配
print(re.match('com', 'www.chenhanpeng.com'))      # 不在起始位置匹配

line = "Cats are smarter than dogs"
# .* 表示任意匹配除换行符（\n、\r）之外的任何单个或多个字符
matchObject = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObject:
    print('matchObject.group() :', matchObject.group())
    print('matchObject.group(1) :', matchObject.group(1))
    print('matchObject.group(2) :', matchObject.group(2))
else:
    print('no match')