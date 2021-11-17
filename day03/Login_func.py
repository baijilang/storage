# 测试主程序
from selenium.webdriver.common.by import By
import time


class HKR_Login:

    # 测试用例执行前优先执行的
    def __init__(self, driver):
        self.driver = driver

    def loginOperate(self, username, password):
        self.driver.find_element(By.XPATH, "//*[@id='loginname']").send_keys(username)
        self.driver.find_element(By.XPATH, "//*[@id = 'password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//*[@id='submit']").click()

    def login_success(self):
        time.sleep(0.5)
        result = self.driver.title
        return result

    def login_default(self):
        result = self.driver.find_element(By.XPATH, "//*[@id='msg_uname']").text
        return result
