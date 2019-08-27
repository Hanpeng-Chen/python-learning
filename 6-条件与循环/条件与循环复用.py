# 我们要绘制y = 2*|x| + 5 的函数图像，给定集合x的数据点，需要计算出y的数据集合
x = [-2, -1, 0, 1, 2]
y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
print(y)


# 将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首尾的空字符，并过滤掉长度小于等于5的单词，最后返回由单词组成的列表
text = ' Today , is, Sunday '
text_list = [s.strip() for s in text.split(',') if len(s) > 5]
print(text_list)



"""
给定下面两个列表attributes和values，要求针对values中每一组子列表value，输出其和attributes中的键对应后的字典，最后返回字典组成的列表。
attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# expected output:
[{'name': 'jason', 'dob': '2000-01-01', 'gender': 'male'}, 
{'name': 'mike', 'dob': '1999-01-01', 'gender': 'male'}, 
{'name': 'nancy', 'dob': '2001-02-01', 'gender': 'female'}]
"""

attributes = ['name', 'dob', 'gender']
values = [['jason', '2000-01-01', 'male'], 
['mike', '1999-01-01', 'male'],
['nancy', '2001-02-01', 'female']
]

# 多行循环语句
output = []
for item in values:
    output_item = {}
    for index in range(0, len(attributes)):
        output_item[attributes[index]] = item[index]
    output.append(output_item)
print(output)

# 一行循环语句
## 实现1
print([dict([(attributes[index], item[index]) for index in range(len(attributes))]) for item in values])
## 实现2
## zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同，利用 * 号操作符，可以将元组解压为列表。
print([dict(zip(attributes,v)) for v in values])