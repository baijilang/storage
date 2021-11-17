# 测试主程序
import os
import time
import unittest
from unittest import TestCase

from ddt import data
from ddt import ddt
from ddt import unpack
from selenium import webdriver

from Case_Login import Login_Default_Case, Login_Success_Case, open_excel
from Login_func import HKR_Login


@ddt
class Test_HKR_Login(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.workbook, cls.sheet, cls.index = open_excel('HkrTestCase.xlsx', 'Login')
        cls.tabledata = Login_Success_Case + Login_Default_Case
        cls.rows = len(Login_Success_Case + Login_Default_Case)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.workbook.save('new.xlsx')
        os.replace('new.xlsx', 'HkrTestCase1.xlsx')

    # 测试用例执行前优先执行的
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/HKR/')

    def tearDown(self):
        self.driver.quit()

    def write_result(self, username, password, exception, result):
        # 遍历用例，找出本次测试的用例
        i, j = 0, self.index
        for row, values in enumerate(self.tabledata):
            if values[:3] == [username, password, exception]:
                # 确定了本条用例再excel表里面的位置，传入结果
                i = row + 1
                break
        if result == exception:
            self.sheet.write(i, j, 'pass')
            self.sheet.write(i,j,time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        else:
            self.sheet.write(i, j, 'fail')
            self.sheet.write(i, j, time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    @data(*Login_Success_Case)
    @unpack
    def test_login_success(self, username, password, exception):
        login = HKR_Login(self.driver)
        login.loginOperate(username, password)
        result = login.login_success()
        time.sleep(1)
        self.write_result(username, password, exception, result)
        self.assertEqual(result, exception)

    @data(*Login_Default_Case)
    @unpack
    def test_login_default(self, username, password, exception):
        login = HKR_Login(self.driver)
        login.loginOperate(username, password)
        result = login.login_default()
        time.sleep(1)
        self.write_result(username, password, exception, result)
        self.assertEqual(result, exception)


if __name__ == '__main__':
    unittest.main()
