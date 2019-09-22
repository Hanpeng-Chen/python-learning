from functools import reduce
# map函数
# 要对列表中的每个元素乘以2，用map可以实现如下：
l = [1, 2, 3, 4, 5]
re = map(lambda x: x * 2, l)
print(list(re))  # [2， 4， 6， 8， 10]


# filter函数
l = [1, 2, 3, 4, 5]
result = filter(lambda x: x % 2 == 1, l)
print(list(result))


# reduce函数
l2 = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x * y, l2)
print(result)