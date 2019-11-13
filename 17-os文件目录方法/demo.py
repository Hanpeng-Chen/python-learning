import os

## 查看当前目录的绝对路径
print(os.path.abspath('./'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来，然后创建一个目录
new_dir = os.path.join('./', 'newdir')
print(new_dir)
os.mkdir(new_dir)

# 删除一个目录
os.rmdir(new_dir)


# 把两个路径合成一个
path1 = os.path.abspath('./')
path2 = 'demo.py'
path = os.path.join(path1, path2)
print(path)  # E:/workspace/python-learning/demo.py

# 拆分路径时
print(os.path.split('E:/workspace/python-learning/demo.py'))  # ('E:/workspace/python-learning', 'demo.py')


# os.path.splitext()直接得到文件扩展名
print(os.path.splitext('E:/workspace/python-learning/demo.py')) # ('E:/workspace/python-learning/demo', '.py')
