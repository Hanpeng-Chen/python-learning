from email.mime.text import MIMEText
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase

import smtplib

# 格式化邮件地址，并用Header对象进行编码（防止包含中文）
def format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

# 输入Email地址和口令
from_address = '****@qq.com'
from_account_password = '********************' # 第三方登录邮箱的授权码，QQ邮箱为16位授权码
# 输入收件人地址
to_address = '****@163.com'

message = MIMEMultipart()
# 设置发件人信息
message['From'] = format_addr('Python开发 <%s>' % from_address)
# 设置收件人信息
message['To'] = format_addr('学员 <%s>' % to_address)
# 设置邮件主题
message['Subject'] = Header('图片在正文中', 'utf-8').encode()

message.attach(MIMEText('这是一封带附件的email', 'plain', 'utf-8'))

with open('./20-1.png', 'rb') as f:
    # 设置附件的MIME和文件名
    mime = MIMEBase('image', 'png', filename='20.png')
    # 加上必要的头信息
    mime.add_header('Content-Disposition', 'attachment', filename='20.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    message.attach(mime)

# 输入SMTP服务器地址
smtp_server = 'smtp.qq.com'
# SMTP协议默认端口为25
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_address, from_account_password)
server.sendmail(from_address, [to_address], message.as_string())
server.quit()