from HTMLTestRunner import HTMLTestRunner
import unittest
import os

from email.mime.text import MIMEText
from email.header import Header
import smtplib


testPack = unittest.defaultTestLoader.discover(os.getcwd(),pattern=r'Test*.py')

runner = HTMLTestRunner.HTMLTestRunner(
    title='HKR测试报告',
    description = '登陆模块的测试报告',
    verbosity= 2,
    stream=open(file='hkrtest.html',mode='w+',encoding='utf-8')
)
runner.run(testPack)

with open(file='hkrtest.html',mode = 'r+',encoding='utf8') as f:
    info = f.read()
    msg=MIMEText(info,'html','utf-8')
    msg['From'] = Header('dl352621346@163.com')
    msg['To'] = Header('1598181578@qq.com')
    msg['Subject'] = Header('HKR_Login测试报告')

server = smtplib.SMTP('smtp.163.com',25)
server.login('dl352621346@163.com','OEFYFBBGZJBTMSTS')
server.sendmail('dl352621346@163.com',['1598181578@qq.com'],msg.as_string())
server.close()
print('success')


