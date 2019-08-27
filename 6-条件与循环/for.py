s = 'hello world'
for char in s:
  print(char)

list = [1, 2, 3, 4, 5]
for item in list:
  print(item)


# 通过range()函数获取索引，再去遍历
l = ['zhangsan', 'lisi', 'wangwu', 'sunliu', 'zhouqi']
for index in range(0, len(l)):
  print(l[index])

# enumerate()函数来遍历集合
for index, item in enumerate(l):
  print('index: {}, value: {}'.format(index, item))


d = {'name': 'jack', 'age': 20, 'gender': 'male'}
# 遍历字典的键
for k in d:
  print(k)


# 遍历字典的值
for val in d.values():
  print(val)

# 遍历字典的键值对
for k, v in d.items():
  print('key: {}, value: {}'.format(k, v))