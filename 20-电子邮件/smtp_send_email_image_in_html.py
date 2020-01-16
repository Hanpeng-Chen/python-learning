#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

# 输入Email地址和口令
from_address = '****@qq.com'
from_account_password = '****************' # 第三方登录邮箱的授权码，QQ邮箱为16位授权码
# 输入收件人地址
to_address = '****@163.com'

msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("Python开发", 'utf-8')
msgRoot['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')
 
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
 
 
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.chenhanpeng.com">代码视界</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
 
# 指定图片为当前目录
fp = open('./20-1.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
 
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)

# 输入SMTP服务器地址
smtp_server = 'smtp.qq.com'
# SMTP协议默认端口为25
server = smtplib.SMTP(smtp_server, 25)
server.login(from_address, from_account_password)
server.sendmail(from_address, [to_address], msgRoot.as_string())
print('邮件发送成功')
server.quit()