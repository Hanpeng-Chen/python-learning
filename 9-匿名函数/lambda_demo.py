square = lambda x: x**2
print(square(5))

sum = lambda x, y: x + y
print(sum(2, 3))


l = [(lambda x: x*x)(x) for in range(10)]
print(l)


l = [(1, 20), (3, 10), (5, 25), (2, 0)]
l.sort(key=lambda x: x[1]) # 按照列表中元组的第二个元素排序
print(l)


def is_odd(n):
    return n % 2 == 1

L = list(filter(is_odd, range(1, 10)))

# lambda改造
new_l = list(filter(lambda x: x % 2 == 1, range(1, 10)))