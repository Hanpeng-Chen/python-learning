# 字符串的写法
name = 'zhang san'
city = "Fujian"


s1 = 'hello world'
s2 = "hello world"
s3 = """hello world"""
print(s1 == s2 == s3) # 返回True说明s1 s2 s3完全一样

# 函数注释用三引号字符串
def function_notes(value1, value2):
  """
  args:
    value1: number
    value2: number
  return
    value1 + value2
  """
  return value1 + value2


# 转义字符
s = 'a\nb\tc\''
print(s)
print(len(s))


# 字符串的索引
text = 'welcom to china'
print(text[0])
print(text[1:4])