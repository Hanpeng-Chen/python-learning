a = [1, 5, 3, 6, 9, 8]
b = sorted(a)
print(a) # [1, 5, 3, 6, 9, 8]
print(b)   # [1, 3, 5, 6, 8, 9]


l = [('b', 2), ('a', 1), ('c', 3), ('d', 4)]
l1 = sorted(l, key=lambda s:s[1])
print(l1)   # [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
l2 = sorted(l, key=lambda s:s[1], reverse=True) # 降序
print(l2)   # [('d', 4), ('c', 3), ('b', 2), ('a', 1)]