import time

from Android_phone import Android_app
from unittest import TestCase
import unittest


url = '127.0.0.1:4723/wd/hub'
param = {
    'deviceName': '127.0.0.1:62001',
    'platformName': 'Android',
    'platformVersion': '5.1.1',
    'appPackage': 'com.sina.weibo',
    'appActivity': 'com.sina.weibo.SplashActivity'
}


class TestAndroid(TestCase):
    # def setUp(self) -> None:
    #     global url, param
    #     self.driver = webdriver.Remote(url, param)
    #
    # def tearDown(self) -> None:
    #     self.driver.quit()

    def test1(self):
        sina = Android_app()
        time.sleep(5)
        sina.video_page()
        b = 1
        self.assertEqual(1, b)


if __name__ == '__main__':
    unittest.main()
