# 初始化了含有 100,000 个元素的产品，并分别计算了使用列表和集合来统计产品价格数量的运行时间
import time
id = [x for x in range(0, 100000)]
price = [x for x in range(200000, 300000)]
products = list(zip(id, price))

def find_unique_price_using_list(products):
  unique_price_list = []
  for _, price in products:
    if price not in unique_price_list:
      unique_price_list.append(price)
  return len(unique_price_list)

def find_unique_price_using_set(products):
  unique_price_set = set()
  for id, price in products:
    unique_price_set.add(price)
  return len(unique_price_set)

# 计算使用列表的时间
start_using_list = time.perf_counter()
find_unique_price_using_list(products)
end_using_list = time.perf_counter()
print("time elapse using list: {}".format(end_using_list - start_using_list))


# 计算使用集合的时间
start_using_set = time.perf_counter()
find_unique_price_using_set(products)
end_using_set = time.perf_counter()
print("time elapse using set: {}".format(end_using_set - start_using_set))
