# 字典的创建
d1 = {'name': 'jack', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jack', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jack'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jack', age=20, gender='male')

print(d1 == d2 == d3 == d4)  # 返回True，说明创建的4个字典是一样的


# 字典的元素访问
d = {'name': 'jack', 'age': 20, 'gender': 'male'}
print(d['name'])
print(d['location'])


# 利用in来判断key是否存在
d = {'name': 'jack', 'age': 20, 'gender': 'male'}
result = 'name' in d
print(result)
result1 = 'location' in d
print(result1)


# 利用get(key, default)函数进行索引
d = {'name': 'jack', 'age': 20, 'gender': 'male'}
get_result = d.get('name')
get_result1 = d.get('location')
get_result2 = d.get('location', 'China')
print(get_result)
print(get_result1)
print(get_result2)


# 字典的增、删、更新操作
## 增加
d5 = {'name': 'jack', 'age': 20}
d5['gender'] = 'male'
d5['dob'] = '1999-01-01'
print(d5)

## 更新
d5['dob'] = '2000-01-01'
print(d5)

## 删除
d5.pop('gender')
print(d5)


# 排序
d6 = {'b': 1, 'a': 2, 'c': 5}
d6_sorted_by_key = sorted(d6.items(), key=lambda x:x[0])
d6_sorted_by_value = sorted(d6.items(), key=lambda x:x[1])
print(d6_sorted_by_key)
print(d6_sorted_by_value)