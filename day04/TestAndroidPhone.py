import time
import unittest
from unittest import TestCase
from Android_phone import Android_app
from ddt import ddt
# from ddt import unpack
from ddt import data
from appium import webdriver
from InItialCase import Android_testcases

success_cases = Android_testcases.success_case
defeat_cases = Android_testcases.defeat_case


@ddt
class TestAndroid(TestCase):
    url = '127.0.0.1:4723/wd/hub'
    param = {
        'deviceName': '127.0.0.1:62001',
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'appPackage': 'com.sina.weibo',
        'appActivity': 'com.sina.weibo.SplashActivity'}

    def setUp(self) -> None:
        self.driver = webdriver.Remote(self.url, self.param)

    def tearDown(self) -> None:
        try:
            self.driver.quit()
        except Exception:
            print('QUIT')

    @data(*success_cases)
    def test_login_success(self, success_data):
        print(success_data)
        sina = Android_app(self.driver)
        time.sleep(5)
        user = success_data['user']
        password = success_data['password']
        expect = success_data['exception']
        result = sina.log_page(user, password)
        self.assertEqual(expect, result)

    @data(*defeat_cases)
    def test_login_defeat(self, defeat_data):
        print('running')
        sina = Android_app(self.driver)
        time.sleep(5)
        user = defeat_data['user']
        password = defeat_data['password']
        expect = defeat_data['exception']
        result = sina.log_page(user, password)
        self.assertEqual(expect, result)


if __name__ == '__main__':
    unittest.main()
