import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from HTMLTestRunner import HTMLTestRunner
from unittest import defaultTestLoader


# 载入测试用例
def getHtml(filename):
    pathStart = os.getcwd()
    testPack = defaultTestLoader.discover(start_dir=pathStart, pattern='Test*.py')
    runner = HTMLTestRunner.HTMLTestRunner(
        title='影院测试',
        description='影院流程测试',
        verbosity=3,
        stream=open(file=filename + '.html', mode='w+', encoding='utf-8')
    )
    runner.run(testPack)
    ...


def sentHtml(filename, from_address, to_address, pwd):
    # 邮件发送
    with open(file=filename + '.html', mode='r+', encoding='utf8') as f:
        info = f.read()
        msg = MIMEText(info, 'html', 'utf-8')
        msg['From'] = Header(from_address)
        msg['To'] = Header(to_address)
        msg['Subject'] = Header('测试报告')
    smtp_server = smtplib.SMTP('smtp.163.com', 25)
    # smtp_server.set_debuglevel(1)
    smtp_server.login(from_address, pwd)
    smtp_server.sendmail(from_address, [to_address], msg.as_string())
    smtp_server.close()
    print('success')


if __name__ == "__main__":
    from_addr = input("from_address:")
    password = input('password:')
    to_addr = input('to_address:')
    file_name = 'TestReport'
    getHtml(file_name)
    sentHtml(file_name, from_addr, to_addr, password)
