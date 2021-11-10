from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
from email.utils import formataddr,parseaddr
import smtplib

from email.mime.base import MIMEBase
from email.header import Header
from email import encoders

def _format_addr(address):
    name,addr = parseaddr(address)
    return formataddr((Header(name,'utf-8').encode,addr))

msg =MIMEMultipart()
msg['From'] = Header(_format_addr(input('From_addr：')))
# msg['password'] = input('password:')
msg['To'] = Header(_format_addr('To_addr:'))
msg['Subject'] = Header('银行测试报告','utf-8').encode()

msg.attach('银行测试报告_bjl','plain','utf-8')


