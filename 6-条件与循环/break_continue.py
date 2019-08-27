for char in 'hello world':
  if char == 'l':
    break
  print(char)


count = 0
while count < 10:
  if count >= 5:
    break
  print(count)
  count += 1


# continue
print('=====continue===========')
for char in 'hello world':
  if char == 'l':
    continue
  print(char)

i = 1
while i < 10:   
    i += 1
    if i%2 > 0:     # 非双数时跳过输出
        continue
    print(i)
