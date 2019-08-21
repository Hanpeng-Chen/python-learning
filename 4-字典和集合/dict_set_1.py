# 用列表来存储这些数据结构，并进行查找
def find_product_price(products, product_id):
  for id, price in products:
    if id == product_id:
      return price
  return None

products = [
  (143121312, 100), 
  (432314553, 30),
  (32421912367, 150)
]
print('The price of product 432314553 is {}'.format(find_product_price(products, 432314553)))


# 使用字典来存储这些数据，并进行查找
products_dict = {
  143121312: 100,
  432314553: 30,
  32421912367: 150
}
print('The price of product 32421912367 is {}'.format(products_dict[32421912367]))


# 使用列表，找出有几种不同的价格
def find_unique_price_using_list(products):
  unique_price_list = []
  for _, price in products:
    if price not in unique_price_list:
      unique_price_list.append(price)
  return len(unique_price_list)

products1 = [
  (143121312, 100), 
  (432314553, 30),
  (32421912367, 150),
  (937153201, 30)
]
print('using list===> number of unique price is {}'.format(find_unique_price_using_list(products1)))



# 使用集合，找出不同价格的个数
def find_unique_price_using_set(products):
  unique_price_set = set()
  for id, price in products:
    unique_price_set.add(price)
  return len(unique_price_set)

products2 = [
  (143121312, 100), 
  (432314553, 30),
  (32421912367, 150),
  (937153201, 30)
]
print('using set===> number of unique price is {}'.format(find_unique_price_using_set(products2)))