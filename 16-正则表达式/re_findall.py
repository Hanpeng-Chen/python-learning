import re

str = 'hello 12356 world! 0'
pattern = re.compile(r'\d+')
result1 = pattern.findall(str)
result2 = pattern.findall(str, 0, 8)
print(result1)
print(result2)