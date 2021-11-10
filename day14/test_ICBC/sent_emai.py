from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr,parseaddr
import smtplib
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders


def _format_addr(address):
    name,addr = parseaddr(address)
    return formataddr((Header(name,'utf-8').encode(),addr))


# from_addr = input('From_addr：')
# password = input('password:')
# to_addr = input('To_addr:')


from_addr = 'dl352621346@163.com'
password = 'OEFYFBBGZJBTMSTS'
to_addr = '1598181578@qq.com'
smtp_server = 'smtp.163.com'


msg =MIMEMultipart()  # 创建文件对象
msg['From'] = (_format_addr(from_addr))  # 设置文件的属性：from、to、subject
msg['To'] = (_format_addr(to_addr))
msg['Subject'] = Header('银行测试报告','utf-8').encode()

msg.attach(MIMEText('银行测试报告_bjl','plain','utf-8'))  # 添加文本的正文

with open(file='test_result.xls',mode='rb') as f:  # 添加附件
    mime = MIMEBase('file','xls',filename='test_result.xls')
    mime.add_header('Content-Disposition','attachment',filename='test_result.xls')
    mime.add_header('Content-ID','<0>')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

server = smtplib.SMTP(smtp_server,25)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.close()
print('success!')








