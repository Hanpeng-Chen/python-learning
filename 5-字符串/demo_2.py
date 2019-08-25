str1 = "hello World!"
# 利用len函数计算字符串长度
print(len(str1)) # 12

# 获取字符串首字母大写的拷贝
print(str1.capitalize()) # Hello world!

# 获取字符串变大写后的拷贝
print(str1.upper()) # HELLO WORLD!

# find函数查找子串的位置
print(str1.find('llo')) # 2
print(str1.find('hot')) # -1
# # index查找子串，但找不到子串或报错
# print(str1.index('llo'))
# print(str1.index('hot'))

# 判断字符串是否以指定的字符串开头
print(str1.startswith('he')) # True
print(str1.startswith('ha')) # False

# 判断字符串是否以指定的字符串结尾
print(str1.endswith('d!')) # True
print(str1.endswith('ld')) # False

# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '='))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, '-'))

str2 = '1234abcd'
# 索引操作
print(str2[3]) # 4
# 字符串切片操作(从指定的位置开始索引)
print(str2[2:5])  # 34a
print(str2[2:])  # 34abcd
print(str2[2::2])  # 3ac
print(str2[::2])  # 13ac
print(str2[::-1])  # dcba4321
print(str2[-3:-1])  # bc

# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True

str3 = '  my name is zhangsan  '
# 获得字符串修剪头尾空格后的拷贝
print(str3.strip())  # my name is zhangsan