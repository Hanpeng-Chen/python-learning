# 创建一个返回数字的迭代器，初始值为0，逐步递增10
class numbers:
    def __iter__(self):
        self.a = 0
        return self

    def __next__(self):
        x = self.a
        self.a += 10
        return x

myclass = numbers()
it = iter(myclass)

print(next(it))
print(next(it))
print(next(it))
print(next(it))