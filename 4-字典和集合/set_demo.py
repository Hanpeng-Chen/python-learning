# 集合的创建
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1 == s2)


# 集合的操作
## 集合不支持索引，下面写法会报错
s = {1, 2, 3}
print(s[0])

## in判断一个元素是否在集合中
s = {1, 2, 3}
print(1 in s)
print(4 in s)


# 增、删、改操作
## 增
s = {1, 2, 3}
s.add(4)
print(s)

# 更新update()
s3 = {3, 4, 5}
s.update(s3)
print(s)

# 从集合中删除元素4
s.remove(4)
print(s)
s.discard(3)
print(s)
s.remove(6) # 元素不存在会报错


# 排序
s4 = {3, 4, 2, 1}
s5 = sorted(s4)
print(s5)