# # 打开一个文件
# f = open('./file_1.txt', 'w')
# f.write('Python是一门有用的编程语言。\nHello world！')
# # 关闭打开的文件
# f.close()


# # f.read()
# f = open('./file_1.txt', 'r')
# str = f.read()
# print(str)
# f.close()


# # f.readline()
# f = open('./file_1.txt', 'r')
# str = f.readline()
# print(str)
# str1 = f.readline()
# print(str1)
# str2 = f.readline()
# print(str2)
# f.close()

# # f.readlines()
# f = open('./file_1.txt', 'r')
# str = f.readlines()
# print(str)  # ['Python是一门有用的编程语言。\n', 'Hello world！']
# f.close()


# # f.write()
# f = open('./file_2.txt', 'w')
# value = ('Python从小白到攻城狮', 666)
# s = str(value)
# f.write(s)
# f.close()