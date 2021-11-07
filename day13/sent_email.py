# 发邮件
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


from_addr = '######@163.com'
password = ‘#########'
to_addr = '########'
smtp_server = 'smtp.163.com'

msg = MIMEMultipart()
msg['From'] = _format_addr(f'"name"<{from_addr}>')
msg['To'] = _format_addr(f'管理员<{to_addr}>')
msg['Subject'] = Header('计算器的测试报告','utf-8').encode()
msg.attach(MIMEText('计算器四则运算测试报告','plain','utf-8'))

with open(file='计算器的测试报告.html',mode='rb') as f:
    mime = MIMEBase('file','html',filename = '计算器的测试报告.html')
    mime.add_header('Content-Disposition', 'attachment', filename='计算器的测试报告.html')
    mime.add_header('Content-ID', '<0>')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server, 25)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
