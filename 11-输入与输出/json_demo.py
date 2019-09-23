import json

data = {
  'name': 'Jack',
  'age': 20,
  'address': 'Fujian, China',
}

data_str = json.dumps(data)
print('after json dumps')
print('type of data_str is {}, data_str = {}'.format(type(data_str), data_str))

origin_data = json.loads(data_str)
print('after json loads')
print('type of origin_data is {}, origin_data = {}'.format(type(origin_data), origin_data))