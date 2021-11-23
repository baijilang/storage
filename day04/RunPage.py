import smtplib
# from unittest import defaultTestLoader
import unittest
from HTMLTestRunner import HTMLTestRunner
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os


def run_case(find_path):
    test_pack = unittest.defaultTestLoader.discover(find_path, pattern=r'Test*.py')
    runner = HTMLTestRunner.HTMLTestRunner(
        title='微博测试',
        description='登录模块测试',
        verbosity=1,
        stream=open('weibo_test.html', mode='w+', encoding='utf-8')
    )
    runner.run(test_pack)


def send_msg(filename, from_addr, password, smtp_server,  interface, to_addr):
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


run_case(os.getcwd())
send_msg('weibo_test.html', 'dl352621346@163.com', 'OEFYFBBGZJBTMSTS', 'smtp.163.com', 25, '1598181578@qq.com')
print('Finish!')
