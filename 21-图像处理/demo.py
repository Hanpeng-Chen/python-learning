from PIL import Image, ImageFilter

# 读取图像
# image = Image.open('./test.jpg')
# print(image.format, image.size, image.mode)
# image.show()

# 修改图片格式
# image1 = Image.open('./test1.jpg').save('test1.png')

# 裁剪图像
# image = Image.open('./test.jpg')
# rect = 80, 20, 310, 360
# image.crop(rect).show()

# # 生成缩略图
# size = 128, 128
# image.thumbnail(size)
# image.show()

# # 黏贴图像
image1 = Image.open('./test.jpg')
image2 = Image.open('./test1.jpg')
rect = 0, 00, 200, 200
image2_head = image2.crop(rect)
image1.paste(image2_head, (172, 40))
image1.show()

# 缩放图片
# image2 = Image.open('./test1.jpg')
# width, height = image2.size
# image2_head.resize((int(width / 1.5), int(height / 1.5))

# # 旋转和翻转
# image = Image.open('./test.jpg')
# image.rotate(180).show()
# image.transpose(Image.FLIP_LEFT_RIGHT).show()

# # 操作像素
# image = Image.open('./res/guido.jpg')
# for x in range(80, 310):
#     for y in range(20, 360):
#         image.putpixel((x, y), (128, 128, 128))

# image.show()

# # 滤镜效果
# image = Image.open('./test1.jpg')
# image.filter(ImageFilter.CONTOUR).show()