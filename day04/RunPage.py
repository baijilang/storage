import smtplib
from unittest import defaultTestLoader
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


def run(find_path):
    try:
        tests = defaultTestLoader.discover(find_path, pattern='Test*.py')
        runner = HTMLTestRunner.HTMLTestRunner(
            title='微博测试',
            description='登录模块测试',
            verbosity=1,
            stream=open('weibo_test.html', 'rw+'))
        runner.run(tests)
    except Exception as e:
        print('error1:', e)
    pass


def send_msg(filename, from_addr, password, smtp_server,  interface,to_addr):
    try:
        # 文件主题对象
        msg = MIMEMultipart()
        msg['From'] = Header(from_addr)
        msg['To'] = Header(to_addr)
        msg['Subject'] = Header('微博登录测试', 'utf-8')

        with open(file=filename, mode='rb+') as f:
            # 实例化一个附件对象
            info = MIMEBase('file', 'html', filename=filename)
            # 对象载入
            info.add_header('Content-Disposition', 'Attachment', filename=filename)
            # 向附件导入内容
            info.set_payload(f.read())
            encoders.encode_base64(info)
            # 添加到主体
            msg.attach(info)

        # 发送邮件
        server = smtplib.SMTP(smtp_server, interface)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.close()
    except Exception as e:
        print(e)
        print('this')
    pass


run(r'C:\Users\Administrator\Desktop\demo\HKRtask\自动化\day04')
send_msg('weibo_test.html', 'xxxxxx@163.com', 'xxxxxxxx', 'smtp.163.com', 25, 'xxxxxxx@qq.com')
print('Finish!')
